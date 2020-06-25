import networkx as nx
import math
from graph_gen_and_visualise import *
from dynamic_programming import *


def dist(x1, y1, x2, y2):
    """
    Regular distance formula for 2 points.
    """
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_graph(coordinates):
    """
    Gets a list of tuples that are x and y co-ordinates of the nodes
    and returns an networkx graph object.
    """
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight=dist(
                coordinates[i][0], coordinates[i][1], coordinates[j][0], coordinates[j][1]))
    return g


def two_approx(g):
    """
    Finds a solution to the TSP for a metric graph of the TSP. A metric TSP is
    one where all edges are undirected and that it is a Euclidian TSP, i.e it
    follows the triangular inequality. Example: for 3 edges u,v,w and W(x,y)
    being the distance from x to y or vice versa: W(u,v) <= W(u,z) + W(v,z).
    This approximation algorithm gaurantees a solution that is at-most two times
    the optimal solution doing so by constructing the MST, a pseudo-Eulerian
    path and then adding nodes accordingly. The pseudo-Eulerian path can be
    achieved by using the dfs_preorder_nodes function.
    """
    mst = nx.minimum_spanning_tree(g)
    dfs = list(nx.dfs_preorder_nodes(mst, 0))
    # print(dfs)
    path = []
    for node in dfs:
        if node not in path:
            path.append(node)
    path.append(path[0])  # final node to make it a cycle
    weight = 0
    for i in range(len(path) - 1):
        weight += g[path[i]][path[i+1]]["weight"]
    return weight, path


def main():
    """
    For this example, it finds the optimal result!
    """
    coordinates = [(181, 243), (101, 143), (100, 216), (167, 15), (37, 201),
                   (163, 226), (2, 42), (35, 73), (85, 116), (142, 235), (200, 18)]
    g = get_graph(coordinates)
    weight, cycle = two_approx(g)
    print(
        f"The approximate optimal weight, as determined by 2-approximation is {weight:.2f} and the path is {cycle}")
    optimal_weight, opt_cycle = dynamic_programming_fn(g)
    print(f"The correct optimal weight is {optimal_weight:.2f} and path is {opt_cycle}.")
    display_graph(g, cycle)


if __name__ == '__main__':
    main()
