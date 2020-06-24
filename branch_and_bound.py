import networkx as nx
import matplotlib.pyplot as plt
from graph_gen_and_visualise import *


def get_lower_bound(g, sub_cycle):
    """
    Attempts to find the lower bound for an optimal solution to the TSP by finding
    the weight of the minimum spanning tree of the nodes presently not in the sub_cycle.
    If the current sub_cycle is 0 nodes or all the nodes, the lower bound is the sum of the
    sub_cycle and MST. Else, the weight is the sum of the sub_cycle, the smallest node connecting
    the last vertex of the sub_cycle to the rest of the graph, the weight of the MST and the
    smallest node connecting the MST to the first node of the sub_cycle.
    """
    weight_cycle = sum([g[sub_cycle[i]][sub_cycle[i+1]]["weight"] for i in range(len(sub_cycle)-1)])
    unused_nodes = [v for v in g.nodes() if v not in sub_cycle]
    h = g.subgraph(unused_nodes)  # to get MST for the unused nodes.
    min_tree = list(nx.minimum_spanning_edges(h))
    mst_weight = sum([h.get_edge_data(e[0], e[1])['weight'] for e in min_tree])
    if not len(sub_cycle) or len(sub_cycle) == g.number_of_nodes():
        return weight_cycle + mst_weight
    # print(len(sub_cycle))
    start, end = sub_cycle[0], sub_cycle[-1]
    min_from_cycle = min([g[end][v]['weight'] for v in g.nodes() if v not in sub_cycle])
    min_to_cycle = min([g[v][start]['weight'] for v in g.nodes() if v not in sub_cycle])
    return weight_cycle + mst_weight + min_from_cycle + min_to_cycle


def branch_and_bound(g, sub_cycle=None, current_min=float("inf"), min_cycle=[]):
    """
    Takes in a graph, the current sub_cycle and the minimum weight currently so
    we do not build paths of greater weight.
    """
    if not sub_cycle:
        sub_cycle = [0]  # starts from 0
    if len(sub_cycle) == g.number_of_nodes():
        sub_cycle.append(sub_cycle[0])
        cycle_weight = sum([g[sub_cycle[i]][sub_cycle[i+1]]["weight"]
                            for i in range(len(sub_cycle)-1)])
        current_cycle = list(sub_cycle)
        return cycle_weight, current_cycle

    unused_nodes = [(g[sub_cycle[-1]][v]['weight'], v) for v in g.nodes() if v not in sub_cycle]
    # sort them by weight so you consider the shortest node first
    unused_nodes = sorted(unused_nodes)
    for dist, node in unused_nodes:
        extended_sub_cycle = list(sub_cycle)
        extended_sub_cycle.append(node)
        if get_lower_bound(g, extended_sub_cycle) < current_min:  # only then will we bother checking
            potential_weight, potential_cycle = branch_and_bound(
                g, extended_sub_cycle, current_min, min_cycle)
            if current_min > potential_weight:
                current_min = potential_weight
                min_cycle = potential_cycle
    return current_min, min_cycle  # shortest cycle weight


def main(n):
    g = draw_graph(n)
    weight, cycle = branch_and_bound(g)
    print("The least weight is {}, and the path to be taken is {}".format(weight, cycle))
    display_graph(g, cycle)


main(8)
