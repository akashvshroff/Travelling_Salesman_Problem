import itertools as it
import random
import networkx as nx


def draw_graph(n):
    g = nx.Graph()
    edges = (n * (n-1))//2
    weights = []
    for i in range(edges):
        weights.append(random.randrange(5, 25))
    connections = it.combinations(range(n), 2)
    for i, (u, v) in enumerate(connections):
        g.add_edge(u, v, weight=weights[i])
    return g
