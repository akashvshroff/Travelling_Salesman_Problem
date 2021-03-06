# Outline:

- This repository contains the different approaches at arriving at a solution to the famous [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) which is essentially (as per Wikipedia) "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?". In mathematical terms, the problem is to find the minimum cost Hamiltonian cycle in a connected graph. The problem is [NP-Hard](https://en.wikipedia.org/wiki/NP-hardness), that is no feasible algorithm that can solve it in polynomial time. The programs in this repository extend upon the extremely unfeasible brute force algorithm which has time complexity of O(n!) where n is the number of nodes. This quickly becomes unfeasible once the number of nodes move into double digits. The programs that I have implemented fall in two categories, exact and approximate. These distinctions as well as the finer nuances of each algorithm are explained in detail below.

# Purpose:

- Studying the intricacies of the Travelling Salesman Problem as well as the different approaches to implementing a solution was the Capstone project in the Discrete Math for CS Specialisation - by UCSD and HSE - that I recently completed. Whilst challenging, the project was extremely engaging and served as an apt introduction into the world of NP-hard and NP-complete problems. The course abstracted a lot of the finer nuances in the implementation of the the programs and I did not feel satisfied so I implemented these programs from scratch and used the functions in the networkx module in order to help users visualise the programs as well!
- Having to implement algorithms such as Branch and Bound, the Held-Karp Algorithm and much more was extremely enriching and taught me the importance of discrete math in every portion of CS, especially in the field of algorithms.

# Description:

- The programs implemented fall in two categories, as mentioned above, exact and approximate. The exact algorithms sacrifice runtime in order to achieve the optimal algorithm and are guaranteed to arrive at the best possible solution although their runtime can vary tremendously, and this is delved into in more detail below. The approximate algorithms are a lot more simple in their execution and are often extremely quick but at the cost of optimality. These algorithms can work fairly well in practice however. Let us consider the two types individually.

- Exact Algorithms:
    - The first exact algorithm to cover is the Branch and Bound approach:
        - While this algorithm is guaranteed to give the best possible solution, its runtime is wholly dependent on the graph that is at hand as in the worst case it is no better than the brute force approach but in general practice, it works rather well.
        - It works through the principle of search tree pruning and at any time, we store the best possible solution thus far and generate more solutions (or branches) node by node. Upon adding any node, we check whether the lower bound of the optimal path that we can get through this branch is lesser than our current minimum cost. If true, then we recursively generate the tree and check at the addition of every node. If false, then we discard the branch and move on. Once the entire branch is generated, if the cost of the branch is less than the minimum cost thus far, we store that value in the minimum cost and store the branch in the current optimal cycle and continue checking all possible branches.
        - Checking the lower bound is the primary heuristic of the Branch and Bound approach and can be reliably checked by ascertaining the cost of the Minimum Spanning Tree of all the nodes that have not yet been used in the current sub-cycle. The proof that the cost of the MST gives the lower bound for the TSP, is rather simple. If you remove an edge from the optimal cycle, you get a tree and the cost of this tree is lower bounded by the cost of the Minimum Spanning Tree - thus the cost of the optimal cycle is lower bounded by the cost of the MST.
        - Once all the branches are checked, we return the current minimum cost and minimum cycle, this is our optimal cost and therefore answer to the TSP.
        - The output produced by the algorithm:
        ![alt-text](https://github.com/akashvshroff/Travelling_Salesman_Problem/blob/master/Example_Images/branch_and_bound.png)
    - The next algorithm we cover is the Dynamic Programming approach to solving the TSP:
        - Better known as the Held Karp algorithm.
        - [Dynamic Programming](https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0#:~:text=Dynamic%20Programming%20(DP)%20is%20an,optimal%20solution%20to%20its%20subproblems) or DP is an algorithmic technique where large problems can be solved by breaking them down into combinations of subproblems and then solving the subproblems leading up to the larger problem. We utilise the fact that the optimal solution to the larger problem is some combination of the optimal solutions to its subproblems.
        - Here that means breaking the nodes into subsets of nodes. For a subset of nodes, which includes the first node: 0 and the last node: i, there exists an optimal path P which could be calculated by a cost function C(S,i). Suppose we consider a vertex j in the subset S. The path linking the first node to j is the optimal path, as it is a portion of P. Therefore C(S,i) = C(S-{i},j) + W(j,i) where W is the distance from j to i. Therefore the problem can be broken down into much smaller problems and we choose j such that it yields the smallest C(S, i).
        - Therefore to solve our larger problem, we have to find the optimal solution to the smaller problems in a recursive relationship as highlighted above.
        - Working with sets in python can be rather tedious at times and therefore, a set can be represented in a binary format. Consider the case of 3 nodes: 0,1,2. To represent a subset of {0,2} we can simply store 101 where a set bit (1) indicates the presence of a node and a 0 indicates absence. Another scenario that becomes much easier is in flipping a bit. To find the C(S,i), we must find C(S - {i},j) and finding the subset without i can be achieved by flipping of the bit at the ith index. This can be done via the XOR operation where S = S ^ (1 << i). To learn more about this representation and bit manipulation, I strongly recommend this video by [William Fiset](https://www.youtube.com/watch?v=cY4HiiFHO1o).
        - In this solution we must generate a 2-D matrix T where the rows represent all nodes from 0 to n-1 and the columns represent all subsets from 0 to 2^n - 1. We therefore also have a few base cases:
            - The cost of going from a node to itself i.e C({0},0) is 0 or + infinity.
            - The cost of going from a node to a subset where it is not present is also + infinity.
            - Another base case, that I have not implemented but could implement is for subsets of length 2 - for example C({0,i},i) is just the distance from 0 to node i. Then we would only range from all subsets of length 3 onwards.
        - An intersection of row and column in the table represents the C(S,i) where S is the column number and the row is i.
        - Once such a table is built we have 2 further operations:
            - Finding minimum cost, or the optimal cost, is the minimum of C(S,i) for all i in range(n) + the cost of getting to i from the starting node, that is node 0.
            - Finding the optimal path - which can be found by working backwards and finding i and j recursively, starting from i = n -1 and ending at i = 0.
            - Here is an image for the path produced when the algorithm is run:
            ![alt-text](https://github.com/akashvshroff/Travelling_Salesman_Problem/blob/master/Example_Images/dynamic_programming.png)

- Approximate Algorithms:
    - These algorithms are thought to be fairly usable in practice and owing to their more feasible time complexity can deal with nodes in the range of millions.
    - The first such algorithm is the Nearest Neighbours algorithm:
        - In this approach, you begin with any node and then add the node that is closest to it, (or the least cost connection). Maintain a list of nodes that have been visited already and if the closest node has already been visited, skip it and add the next closest node.
        - Continue this process until a path that has the same length as the number of nodes has been built, following which you append the first node to the path to create a cycle.
        - While this algorithm works fairly okay in practice, for a Euclidian TSP, this approach returns a cost that is roughly log(n) times worse than the optimal where n is the number of nodes in the graph.
        - Output of the graph, as you can see, it is not the optimal solution:
        ![alt-text](https://github.com/akashvshroff/Travelling_Salesman_Problem/blob/master/Example_Images/nearest_neighbour.png)
    - 2-Approximation:
        - This approach to solving the TSP returns a solution that is at most twice the optimal cost.
        - The steps to it are as follows:
            - Construct the Minimum Spanning Tree of the graph.
            - Double every edge, i.e if an edge exists between vertices u,v; add another edge between u and v.
            - Thereby the degree of all vertices becomes even and therefore we can find the Eulerian path - a path that visits every edge only once. This can be done through a simple [Depth First Search](http://www.graph-magics.com/articles/euler.php) algorithm.
            - Loop through the path that is generated by the DFS and keep adding the nodes to a separate approximate_path variable if they are not already in the approximate_path variable. Once it is over, append the first node to the end of the path to create a cycle.
            - Loop through it to generate the weight of the cycle.

## P.S:
- The graph_gen_and_visualise program randomly generates the graphs and helps visualise them using matplotlib and networkx to better understand the algorithms and the larger TSP.
