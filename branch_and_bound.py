import networkx as nx


def get_lower_bound(g, subcycle):
    """
    Attempts to find the lower bound for an optimal solution to the TSP by finding
    the weight of the minimum spanning tree of the nodes presently not in the subcycle.
    If the current subcycle is 0 nodes or all the nodes, the lower bound is the sum of the
    subcycle and MST. Else, the weight is the sum of the subcycle, the smallest node connecting
    the last vertex of the subcycle to the rest of the graph, the weight of the MST and the
    smallest node connecting the MST to the first node of the subcycle.
    """
    weight_cycle = sum([g[subcycle[i]][subcycle[i+1]]["weight"] for i in range(len(subcycle)-1)])
    unused_nodes = [v for v in g.nodes() if v not in subcycle]
    h = g.Graph(unused)  # to get MST for the unused nodes.
    min_tree = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in min_tree])
    if len(subcycle) in [0, g.number_of_nodes()]:
        return weight_cycle + mst_weight
    start, end = subcycle[0], subcycle[-1]
    min_from_cycle = min([g[end][v]['weight'] for v in unused_nodes])
    min_to_cycle = min(g[v][start]['weight'] for v in unused_nodes])
    return weight_cycle + mst_weight + min_from_cycle + min_to_cycle

def branch_and_bound(g, sub_cycle=None, current_min = float("inf")):
    """
    Takes in a graph, the current sub_cycle and the minimum weight currently so
    we do not build paths of greater weight.
    """
    if not sub_cycle:
        sub_cycle= [0]  # starts from 0
    if len(sub_cycle) == g.number_of_nodes():
        sub_cycle.append(sub_cycle[0])
        cycle_weight= sum([g[sub_cycle[i]][sub_cycle[i+1]]["weight"] for i in range(len(sub_cycle)-1)])
        return weight
    unused_nodes= [(g[sub_cycle[-1]][v]['weight'], v) for v in g.nodes() if v not in sub_cycle]
    unused_nodes= sorted(unused_nodes)  # sort them by weight so you consider the shortest node first
    for dist, node in unused_nodes:
        extended_subcycle = sub_cycle[:: ]
        extended_subcycle.append(node)
        if get_lower_bound(g, extended_subcycle) < current_min:  # only then will we bother checking
            potential_weight= branch_and_bound(g, extended_subcycle, current_min)
            if current_min > potential_weight:
                current_min= potential_weight
    return current_min  # shortest cycle weight
