# Outline:

- This repository contains the different approaches at arriving at a solution to the famous [Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) which is essentially (as per Wikipedia) "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?". In mathematical terms, the problem is to find the minimum cost Hamiltonian cycle in a connected graph. The problem is [NP-Hard](https://en.wikipedia.org/wiki/NP-hardness), that is no feasible algorithm that can solve it in polynomial time. The programs in this repository extend upon the extremely unfeasible brute force algorithm which has time complexity of O(n!) where n is the number of nodes. This quickly becomes unfeasible once the number of nodes move into double digits. The programs that I have implemented fall in two categories, exact and approximate. These distinctions as well as the finer nuances of each algorithm are explained in detail below.

# Purpose:

- Studying the intricacies of the Travelling Salesman Problem as well as the different approaches to implementing a solution was the Capstone project in the Discrete Math for CS Specialisation - by UCSD and HSE - that I recently completed. Whilst challenging, the project was extremely engaging and served as an apt introduction into the world of NP-hard and NP-complete problems. The course abstracted a lot of the finer nuances in the implementation of the the programs and I did not feel satisfied so I implemented these programs from scratch and used the functions in the networkx module in order to help users visualise the programs as well!
- Having to implement algorithms such as Branch and Bound, the Held-Karp Algorithm and much more was extremely enriching and taught me the importance of discrete math in every portion of CS, especially in the field of algorithms.

# Description:

- The programs implemented fall in two categories, as mentioned above, exact and approximate. The exact algorithms sacrifice runtime in order to achieve the optimal algorithm and are guaranteed to arrive at the best possible solution although their runtime can vary tremendously, and this is delved into in more detail below. The approximate algorithms are a lot more simple in their execution and are often extremely quick but at the cost of optimality. These algorithms can work fairly well in practice however. Let us consider the two types individually.
- Exact Algorithms:
    -
