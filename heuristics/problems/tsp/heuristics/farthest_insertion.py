import math
from ..problem import TSP

def farthest_insertion_heuristic(problem: TSP, start_node: int) -> tuple[list[int], float]:
    """Generates a solution for the TSP problem using the farthest insertion heuristic.

    The farthest insertion heuristic starts at one node and then, repeatedly finds the 
    node not already in the tour that is farthest from any node in the tour. It then 
    inserts the node into the position that minimizes the increase in the total cost. 
    It stops when all nodes have been visited.

    The time complexity of the farthest insertion algorithm is O(n^2).

    :param problem: The TSP problem.
    :param start_node: The node to start the solution from.
    :return: A solution obtained with the farthest insertion heuristic and its cost.
    """
    solution = [start_node]
    nodes = problem.nodes()
    nodes.remove(start_node)
    while len(nodes) > 0:

        # Find the non-visited node that is farthest from any node in the current solution
        farthest_node = None
        farthest_cost = -math.inf
        for node in nodes:
            min_distance = math.inf
            for solution_node in solution:
                distance = problem.cost(node, solution_node)
                if distance < min_distance:
                    min_distance = distance
            if min_distance > farthest_cost:
                farthest_node = node
                farthest_cost = min_distance

        # Insert the farthest node into a position that minimizes the increase in cost
        best_index = len(solution)
        best_cost = math.inf
        for i in range(len(solution)):
            cost = (problem.cost(solution[i - 1], farthest_node) +
                    problem.cost(farthest_node, solution[i]) -
                    problem.cost(solution[i - 1], solution[i]))
            if cost < best_cost:
                best_index = i
                best_cost = cost

        # Update the solution and the list of nodes
        solution.insert(best_index, farthest_node)
        nodes.remove(farthest_node)

    return solution, problem.evaluate(solution)
