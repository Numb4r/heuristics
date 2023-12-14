import math
from ..problem import TSP


def nearest_neighbor_heuristic(
    problem: TSP,
    start_node: int
) -> tuple[list[int], float]:
    """Generates a solution for the TSP problem using the nearest neighbor heuristic.

    The nearest neighbor heuristic starts at one node and connects with the closests 
    unvisited node. It repeats until all nodes have been visited. It then returns to 
    the starting node.

    The time complexity of the nearest neighbor algorithm is O(n^2).

    :param TSP: The TSP problem.
    :param start_node: The node to start the solution from.
    :return: A solution obtained with the nearest neighbor heuristic and its cost.
    """
    solution = [start_node]
    nodes = problem.nodes()
    nodes.remove(start_node)

    while len(nodes) > 0:
        last_node = solution[-1]
        best_node = None
        best_cost = math.inf
        for node in nodes:
            cost = problem.cost(last_node, node)
            if cost < best_cost:
                best_node = node
                best_cost = cost
        solution.append(best_node)
        nodes.remove(best_node)

    return solution, problem.evaluate(solution)
