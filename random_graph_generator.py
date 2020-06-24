import itertools as it
import random
import networkx as nx
import matplotlib.pyplot as plt


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


def display_graph(g, path):
    coloured_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    # print(coloured_edges)
    pos = nx.spring_layout(g)
    labels = nx.get_edge_attributes(g, 'weight')
    nx.draw(g, pos)
    nx.draw_networkx_edges(g, pos)
    nx.draw_networkx_edges(g, pos, edgelist=coloured_edges, edge_color='#5fdde5')
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
    plt.show()
