import networkx as nx
from graph_gen_and_visualise import *
import numpy as np


def find_optimal_cost(g, memo, n):
    """
    Returns the most optimal cost, by bruteforcing all the candidates of a tour,
    adding the weight back to 0 (first node) and then returning the minimum value.
    """
    end = (1 << n)-1  # number of subsets
    return min(memo[i][end] + g[0][i]['weight'] for i in range(1, n))


def find_optimal_tour(g, memo, n):
    """
    HELD-KARP ALGORITHM:
    Finds the optimal tour from working backwards from the last node to the
    first node. Here, both are 0. We keep track of the current state
    (which initially is all nodes visited). The variable index tracks the best
    node. If any variable is better then it adds it to the tour and flips off
    the node.
    """
    last_index = 0
    min_tour, end_state = [None for _ in range(n+1)], (1 << n) - 1
    for i in range(n-1, 0, -1):
        index = -1
        for j in range(1, n):
            if not (end_state >> j) & 1:
                continue
            if index == -1:
                index = j
            prev_dist = memo[index][end_state] + g[index][last_index]['weight']
            new_dist = memo[j][end_state] + g[j][last_index]['weight']
            if new_dist < prev_dist:
                index = j
        min_tour[i] = index
        end_state = end_state ^ (1 << index)
        last_index = index
    min_tour[0], min_tour[-1] = 0, 0
    return min_tour


def dynamic_programming_fn(g):
    """
    The function inputs a graph and returns the shortest path as calculated by a dynamic
    programming approach. The function uses a binary notation to
    represent sets where a 1 indicates presence in a set and 0 indicates
    absence.The 2-d array T is initialised with values of infinity and the
    rows are vertices and columns are the possible sets.
    """
    n = g.number_of_nodes()
    T = [[float("inf")] * (1 << n) for _ in range(n)]  # setting up the table
    T[0][1] = 0  # initialise
    for s in range(1 << n):  # looping through all the subsets
        # print("-"*15)
        # print(np.matrix(T))
        if not s & 1 or not bin(s).count('1') > 1:  # sets of length more than 1
            # 0 in the subset
            continue
        for i in range(1, n):
            if not ((s >> i) & 1):  # if i not in subset
                continue
            for j in range(n):
                if j == i or not((s >> j) & 1):  # j equal to i or j not in the subset
                    continue
                T[i][s] = min(T[i][s], T[j][s ^ (1 << i)] + g[i][j]['weight'])
    opt_cost = find_optimal_cost(g, T, n)
    opt_tour = find_optimal_tour(g, T, n)
    return opt_cost, opt_tour


def main(n):
    g = draw_graph(n)
    weight, cycle = dynamic_programming_fn(g)
    print("Optimal cost is {}, and the corresponding cycle is {}".format(weight, cycle))
    display_graph(g, cycle)


if __name__ == "__main__":
    main(5)
