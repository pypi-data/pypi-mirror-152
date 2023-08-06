"""An implementation of the Wasserstein metric between two compositional vectors.
Aka Earth Mover's distance, an appropriate metric for comparing two PDDs.

Copyright (C) 2020 Cameron Hargreaves. This code is part of the Element Movers
Distance project https://github.com/lrcfmd/ElMD.
"""

import numba
import numpy as np


@numba.njit(cache=True)
def network_simplex(source_demands, sink_demands, network_costs):
    """
    This is a port of the network simplex algorithm implented by Loïc Séguin-C
    for the networkx package to allow acceleration via the numba package.
    Copyright (C) 2010 Loïc Séguin-C. loicseguin@gmail.com
    All rights reserved.
    BSD license.
    References
    ----------
    .. [1] Z. Kiraly, P. Kovacs.
           Efficient implementation of minimum-cost flow algorithms.
           Acta Universitatis Sapientiae, Informatica 4(1):67--118. 2012.
    .. [2] R. Barr, F. Glover, D. Klingman.
           Enhancement of spanning tree labeling procedures for network
           optimization.
           INFOR 17(1):16--34. 1979.
    """

    n_sources, n_sinks = source_demands.shape[0], sink_demands.shape[0]
    network_costs = network_costs.ravel()

    # Constant used throughout for conversions from floating point to integer
    fp_multiplier = np.array([1000000], dtype=np.int64)

    # Add one additional node for a dummy source and sink
    nodes = np.arange(n_sources + n_sinks).astype(np.int64)

    # Multiply by a large number and cast to int to remove floating points
    source_d_fp = source_demands * fp_multiplier.astype(np.int64)
    source_d_int = source_d_fp.astype(np.int64)
    sink_d_fp = sink_demands * fp_multiplier.astype(np.int64)
    sink_d_int = sink_d_fp.astype(np.int64)

    # FP conversion error correction
    source_sum = np.sum(source_d_int)
    sink_sum = np.sum(sink_d_int)

    if  source_sum < sink_sum:
        source_ind = np.argmax(source_d_int)
        source_d_int[source_ind] += sink_sum - source_sum
    elif sink_sum < source_sum:
        sink_ind = np.argmax(sink_d_int)
        sink_d_int[sink_ind] += source_sum - sink_sum

    # Create demands array
    demands = np.concatenate((-source_d_int, sink_d_int)).astype(np.int64)

    # Create fully connected arcs between all sources and sinks
    conn_tails = np.array([i for i in range(n_sources) for _ in range(n_sinks)],
                          dtype=np.int64)
    conn_heads = np.array([j + n_sources for _ in range(n_sources) for j in range(n_sinks)],
                          dtype=np.int64)

    # Add arcs to and from the dummy node
    dummy_tails = []
    dummy_heads = []

    for node, demand in np.ndenumerate(demands):
        if demand > 0:
            dummy_tails.append(node[0])
            dummy_heads.append(-1)
        else:
            dummy_tails.append(-1)
            dummy_heads.append(node[0])

    # Concatenate these all together
    tails = np.concatenate((conn_tails, np.array(dummy_heads).T)).astype(np.int64)
    heads = np.concatenate((conn_heads, np.array(dummy_heads).T)).astype(np.int64)  # edge targets

    # Create costs and capacities for the arcs between nodes
    network_costs = network_costs * fp_multiplier
    network_capac = np.array([np.array([source_demands[i], sink_demands[j]]).min()
                              for i in range(n_sources)
                              for j in range(n_sinks)],
                             dtype=np.float64) * fp_multiplier

    # TODO finish?
    # If there is only one node on either side we can return capacity and costs
    # if sources.shape[0] == 1 or sinks.shape[0] == 1:
    #     tot_costs = np.array([cost * network_capac[i_ret] for i_ret, cost in np.ndenumerate(network_costs)], dtype=np.float64)
    #     return np.float64(np.sum(tot_costs))

    # inf_arr = (np.sum(network_capac.astype(np.int64)), np.sum(np.absolute(network_costs)), np.max(np.absolute(demands)))

    # Set a suitably high integer for infinity
    faux_inf = 3 * np.max(np.array((np.sum(network_capac.astype(np.int64)),
                                    np.sum(np.absolute(network_costs)),
                                    np.max(np.absolute(demands))),
                                   dtype=np.int64))

    # Add the costs and capacities to the dummy nodes
    costs = np.concatenate((network_costs, np.ones(nodes.shape[0]) * faux_inf)).astype(np.int64)
    capac = np.concatenate((network_capac, np.ones(nodes.shape[0]) * fp_multiplier)).astype(np.int64)

    # Construct the initial spanning tree.
    e = conn_tails.shape[0]
    n = nodes.shape[0]

    # Initialise zero flow in the connected arcs, and full flow to the dummy
    flows = np.concatenate((np.zeros(e), np.array([abs(d) for d in demands]))).astype(np.int64)

    # General arrays for the spanning tree
    potentials = np.array([faux_inf if d <= 0 else -faux_inf for d in demands]).T
    parent = np.concatenate((np.ones(n) * -1, np.array([-2]))).astype(np.int64)
    edge = np.arange(e, e + n).astype(np.int64)
    size = np.concatenate((np.ones(n), np.array([n + 1]))).astype(np.int64)
    next_node = np.concatenate((np.arange(1, n), np.array([-1, 0]))).astype(np.int64)
    prev_node = np.arange(-1, n)          # previous nodes in depth-first thread
    last_node = np.concatenate((np.arange(n), np.array([n - 1]))).astype(np.int64)  # last descendants in depth-first thread
    f = 0

    ###########################################################################
    # Main Pivot loop
    ###########################################################################

    while True:
        i, p, q, f = find_entering_edges(e, f, tails, heads, costs, potentials, flows)
        if p == -1: # If no entering edges then the optimal score is found
            break

        cycle_nodes, cycle_edges = find_cycle(i, p, q, size, edge, parent)
        j, s, t = find_leaving_edge(cycle_nodes, cycle_edges, capac, flows, tails, heads)
        augment_flow(cycle_nodes, cycle_edges, residual_capacity(j, s, capac, flows, tails), tails, flows)

        if i != j:  # Do nothing more if the entering edge is the same as the leaving edge.
            if parent[t] != s:
                # Ensure that s is the parent of t.
                s, t = t, s

            if np.where(cycle_edges == i)[0][0] > np.where(cycle_edges == j)[0][0]:
                # Ensure that q is in the subtree rooted at t.
                p, q = q, p

            remove_edge(s, t, size, prev_node, last_node, next_node, parent, edge)
            make_root(q, parent, size, last_node, prev_node, next_node, edge)
            add_edge(i, p, q, next_node, prev_node, last_node, size, parent, edge)
            update_potentials(i, p, q, heads, potentials, costs, last_node, next_node)

    # final_emd, final_flows = emd_from_flows_and_costs(flows[:e], costs[:e], fp_multiplier)
    # return final_emd, final_flows
    
    flow_cost = 0
    final_flows = flows[:e].astype(np.float64)
    edge_costs = costs[:e].astype(np.float64)

    # dot product is returning wrong values for some reason...
    for arc_ind, flow in np.ndenumerate(final_flows):
        flow_cost += flow * edge_costs[arc_ind]

    final = flow_cost / fp_multiplier
    final = final.astype(np.float64)
    final = final / fp_multiplier

    final_flows = final_flows / fp_multiplier

    return final[0], final_flows


@numba.njit(cache=True)
def reduced_cost(i, costs, potentials, tails, heads, flows):
    """Return the reduced cost of an edge i.
    """
    c = costs[i] - potentials[tails[i]] + potentials[heads[i]]

    if flows[i] == 0:
        return c
    else:
        return -c


@numba.njit(cache=True)
def find_entering_edges(e, f, tails, heads, costs, potentials, flows):
    """Yield entering edges until none can be found.
    """
    # Entering edges are found by combining Dantzig's rule and Bland's
    # rule. The edges are cyclically grouped into blocks of size B. Within
    # each block, Dantzig's rule is applied to find an entering edge. The
    # blocks to search is determined following Bland's rule.

    B = np.int64(np.ceil(np.sqrt(e))) # block size

    M = (e + B - 1) // B    # number of blocks needed to cover all edges
    m = 0

    while m < M:
        # Determine the next block of edges.
        l = f + B
        if l <= e:
            edge_inds = np.arange(f, l)
        else:
            l -= e
            edge_inds = np.concatenate((np.arange(f, e), np.arange(l)))

        f = l

        # Find the first edge with the lowest reduced cost.
        r_costs = np.empty(edge_inds.shape[0])

        for y, z in np.ndenumerate(edge_inds):
            r_costs[y] = reduced_cost(z, costs, potentials, tails, heads, flows)

        # This takes the first occurrence which should stop cycling
        h = np.argmin(r_costs)

        i = edge_inds[h]
        c = reduced_cost(i, costs, potentials, tails, heads, flows)

        p = q = -1

        if c >= 0:
            m += 1

        # Entering edge found.
        else:
            if flows[i] == 0:
                p = tails[i]
                q = heads[i]
            else:
                p = heads[i]
                q = tails[i]

            return i, p, q, f

    # All edges have nonnegative reduced costs. The flow is optimal.
    return -1, -1, -1, -1


@numba.njit(cache=True)
def find_apex(p, q, size, parent):
    """Find the lowest common ancestor of nodes p and q in the spanning
    tree.
    """
    size_p = size[p]
    size_q = size[q]

    while True:
        while size_p < size_q:
            p = parent[p]
            size_p = size[p]
        while size_p > size_q:
            q = parent[q]
            size_q = size[q]
        if size_p == size_q:
            if p != q:
                p = parent[p]
                size_p = size[p]
                q = parent[q]
                size_q = size[q]
            else:
                return p


@numba.njit(cache=True)
def trace_path(p, w, edge, parent):
    """Return the nodes and edges on the path from node p to its ancestor
    w.
    """
    cycle_nodes = [p]
    cycle_edges = []

    while p != w:
        cycle_edges.append(edge[p])
        p = parent[p]
        cycle_nodes.append(p)

    return cycle_nodes, cycle_edges


@numba.njit(cache=True)
def find_cycle(i, p, q, size, edge, parent):
    """Return the nodes and edges on the cycle containing edge i == (p, q)
    when the latter is added to the spanning tree.
    The cycle is oriented in the direction from p to q.
    """
    w = find_apex(p, q, size, parent)
    cycle_nodes, cycle_edges = trace_path(p, w, edge, parent)
    cycle_nodes = np.array(cycle_nodes[::-1])
    cycle_edges = np.array(cycle_edges[::-1])

    if cycle_edges.shape[0] < 1:
        cycle_edges = np.concatenate((cycle_edges, np.array([i])))

    elif cycle_edges[0] != i:
        cycle_edges = np.concatenate((cycle_edges, np.array([i])))

    cycle_nodes_rev, cycle_edges_rev = trace_path(q, w, edge, parent)

    cycle_nodes = np.concatenate((cycle_nodes, np.int64(cycle_nodes_rev[:-1])))
    cycle_edges = np.concatenate((cycle_edges, np.int64(cycle_edges_rev)))

    return cycle_nodes, cycle_edges


@numba.njit(cache=True)
def residual_capacity(i, p, capac, flows, tails):
    """Return the residual capacity of an edge i in the direction away
    from its endpoint p.
    """
    if tails[np.int64(i)] == np.int64(p):
        return capac[np.int64(i)] - flows[np.int64(i)]

    else:
        return flows[np.int64(i)]


@numba.njit(cache=True)
def find_leaving_edge(cycle_nodes, cycle_edges, capac, flows, tails, heads):
    """Return the leaving edge in a cycle represented by cycle_nodes and
    cycle_edges.
    """
    cyc_edg_rev = np.flip(cycle_edges)
    cyc_nod_rev = np.flip(cycle_nodes)

    res_caps = []
    i = 0
    for edg in cyc_edg_rev:
        res_caps.append(residual_capacity(edg, cyc_nod_rev[i], capac, flows, tails))
        i += 1

    res_caps = np.array(res_caps)

    j = cyc_edg_rev[np.argmin(res_caps)]
    s = cyc_nod_rev[np.argmin(res_caps)]

    t = heads[np.int64(j)] if tails[np.int64(j)] == s else tails[np.int64(j)]
    return j, s, t


@numba.njit(cache=True)
def augment_flow(cycle_nodes, cycle_edges, f, tails, flows):
    """Augment f units of flow along a cycle representing Wn with cycle_edges.
    """
    for i, p in zip(cycle_edges, cycle_nodes):
        if tails[np.int64(i)] == np.int64(p):
            flows[np.int64(i)] += f
        else:
            flows[np.int64(i)] -= f


@numba.njit(cache=True)
def trace_subtree(p, last_node, next_node):
    """Yield the nodes in the subtree rooted at a node p.
    """
    tree = []
    tree.append(p)

    l = last_node[p]
    while p != l:
        p = next_node[p]
        tree.append(p)

    return np.array(tree, dtype=np.int64)


@numba.njit(cache=True)
def remove_edge(s, t, size, prev, last, next_node, parent, edge):
    """Remove an edge (s, t) where parent[t] == s from the spanning tree.
    """
    size_t = size[t]
    prev_t = prev[t]
    last_t = last[t]
    next_last_t = next_node[last_t]
    # Remove (s, t).
    parent[t] = -2
    edge[t] = -2
    # Remove the subtree rooted at t from the depth-first thread.
    next_node[prev_t] = next_last_t
    prev[next_last_t] = prev_t
    next_node[last_t] = t
    prev[t] = last_t

    # Update the subtree sizes and last descendants of the (old) ancestors
    # of t.
    while s != np.int64(-2):
        size[s] -= size_t
        if last[s] == last_t:
            last[s] = prev_t
        s = parent[s]


@numba.njit(cache=True)
def make_root(q, parent, size, last, prev, next_node, edge):
    """
    Make a node q the root of its containing subtree.
    """
    ancestors = []
    # -2 means node is checked
    while q != np.int64(-2):
        ancestors.append(q)
        q = parent[q]
    ancestors.reverse()

    ancestors_min_last = ancestors[:-1]
    next_ancs = ancestors[1:]

    for p, q in zip(ancestors_min_last, next_ancs):
        size_p = size[p]
        last_p = last[p]
        prev_q = prev[q]
        last_q = last[q]
        next_last_q = next_node[last_q]

        # Make p a child of q.
        parent[p] = q
        parent[q] = -2
        edge[p] = edge[q]
        edge[q] = -2
        size[p] = size_p - size[q]
        size[q] = size_p

        # Remove the subtree rooted at q from the depth-first thread.
        next_node[prev_q] = next_last_q
        prev[next_last_q] = prev_q
        next_node[last_q] = q
        prev[q] = last_q

        if last_p == last_q:
            last[p] = prev_q
            last_p = prev_q

        # Add the remaining parts of the subtree rooted at p as a subtree
        # of q in the depth-first thread.
        prev[p] = last_q
        next_node[last_q] = p
        next_node[last_p] = q
        prev[q] = last_p
        last[q] = last_p


@numba.njit(cache=True)
def add_edge(i, p, q, next_node, prev_node, last, size, parent, edge):
    """Add an edge (p, q) to the spanning tree where q is the root of a
    subtree.
    """
    last_p = last[p]
    next_last_p = next_node[last_p]
    size_q = size[q]
    last_q = last[q]
    # Make q a child of p.
    parent[q] = p
    edge[q] = i
    # Insert the subtree rooted at q into the depth-first thread.
    next_node[last_p] = q
    prev_node[q] = last_p
    prev_node[next_last_p] = last_q
    next_node[last_q] = next_last_p

    # Update the subtree sizes and last descendants of the (new) ancestors
    # of q.
    while p != np.int64(-2):
        size[p] += size_q
        if last[p] == last_p:
            last[p] = last_q
        p = parent[p]


@numba.njit(cache=True)
def update_potentials(i, p, q, heads, potentials, costs, last_node, next_node):
    """Update the potentials of the nodes in the subtree rooted at a node
    q connected to its parent p by an edge i.
    """
    if q == heads[i]:
        d = potentials[p] - costs[i] - potentials[q]
    else:
        d = potentials[p] + costs[i] - potentials[q]

    tree = trace_subtree(q, last_node, next_node)
    for q in tree:
        potentials[q] += d
