# Traveling Salesman Problem

The Traveling Salesman Problem (TSP) is a classic optimization problem in the field of combinatorial optimization. It is often used as a benchmark for testing optimization algorithms and serves as a representative example of a broader class of problems known as "NP-hard" problems.

In the TSP, the goal is to find the shortest possible route that visits a given set of cities exactly once and returns to the starting city.

This package contains some sets of instances for the TSP.
- **TSPLIB95:** TSPLIB is a well known library of instances for the TSP and related problems [1]. It is freely available for download from [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/). The format of the instances are described in the [2].
- **Tetrahedron Instances (Tnm):** A library of TSP instances proposed by in [3] which are composed by a family of Euclidean instances for the TSP for which the integrality ratio of the subtour LP converges to 4/3. These instances turn out to be very hard to solve with exact TSP solvers. This library provides instances with up to 200 vertices in TSPLIB format. The authors also provide the code for generating these instances for an arbitrary number of vertices. They can be downloaded from [https://www.or.uni-bonn.de/~hougardy/HardTSPInstances.html](https://www.or.uni-bonn.de/~hougardy/HardTSPInstances.html).

## References

[1] TSPLIB: library of Traveling Salesman Problem. [Online]. Available: [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/), [Accessed: August 12, 2023].

[2] Gerhard Reinelt. "TSPLIB95". Technical report, Universität Heidelberg, 2005. Available: [http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf), [Accessed: August 12, 2023]. 

[3] Stefan Hougardy and Xianghui Zhong. "Hard to solve instances of the Euclidean Traveling Salesman Problem". Mathematical Programming Computation, v.13, 51-74, 2021.
