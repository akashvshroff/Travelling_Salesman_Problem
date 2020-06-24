import networkx as nx
from graph_gen_and_visualise import *
import numpy as np


def dynamic_programming(g):
    n = g.number_of_nodes()
    T = [[float("inf")] * (1 << n) for _ in range(n)]
    T[0][1] = 0
    for s in range(1 << n):
        if not s & 1 or not bin(s).count('1') > 1:
            continue
        for i in range(1, n):
            if not ((s >> i) & 1):  # if i not in subset
                continue
            for j in range(n):
                if j == i or not((s >> j) & 1):  # j equal to i or j not in the subset
                    continue
                T[i][s] = min(T[i][s], T[j][s ^ (1 << i)] + g[i][j]['weight'])
    return min(T[i][(1 << n)-1] + g[0][i]['weight'] for i in range(1, n))


def main(n):
    g = draw_graph(n)
    weight = dynamic_programming(g)
    print(weight)


main(5)
