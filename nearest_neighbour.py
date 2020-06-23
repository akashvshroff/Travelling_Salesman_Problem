import networkx as nx


def nearest_neighbour(g):
    """
    The function takes in a graph as the parameter and returns the weight of the
    minimum Hamiltonian cycle, as explained in the README. It works by choosing the
    least weight or closest node that it has node visited yet until it has visited all nodes.
    For ease of use, the nodes are [0->n-1] where n is the number of nodes in graph g. The edges
    are undirected and weighted.
    """
    n = g.number_of_nodes()
    current_node = 0
    path = [current_node]
    for choice in range(n-1):  # repeat the process n-1 times
        next_node, min_edge = None, float("inf")
        # min edge is the distance to the closest vertex
        for v in g.nodes():  # choose closest vertex
            curr_weight = g[current_node][v]['weight']
            if v not in path and curr_weight < min_edge:
                next_node, min_edge = v, curr_weight
        path.append(next_node)
        current_node = next_node
    path.append(path[-1])  # cycle so add the first element
    weight = sum(g[path[i]][path[i+1]]['weight'] for i in range(len(path)-1))
    return weight
