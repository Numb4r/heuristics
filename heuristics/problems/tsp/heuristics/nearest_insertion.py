import math
from ..problem import TSP


def nearest_insertion_heuristic(problem: TSP, start_node: int) -> tuple[list[int], float]:
    """Generates a solution for the TSP problem using the nearest insertion heuristic.

    The nearest insertion heuristic starts at one node and then, repeatedly finds the 
    node not already in the tour that is closest to any node in the tour. It then 
    inserts the node into the position that minimizes the increase in the total cost. 
    It stops when all nodes have been visited.

    The time complexity of the nearest insertion algorithm is O(n^2).

    :param problem: The TSP problem.
    :param start_node: The node to start the solution from.
    :return: A solution obtained with the nearest insertion heuristic and its cost.
    """
    solution = [start_node]
    nodes = problem.nodes()
    nodes.remove(start_node)
    while len(nodes) > 0:

        # Find the non-visited node that is the closest to a visited node
        best_node = None
        best_cost = math.inf
        for node in nodes:
            for solution_node in solution:
                cost = problem.cost(node, solution_node)
                if cost < best_cost:
                    best_node = node
                    best_cost = cost
        
        # Insert node into a position that minimizes the increase in the cost
        best_index = len(solution)
        best_cost = math.inf
        if (len(solution) > 1):
            for i in range(0, len(solution) ):
                cost = (problem.cost(solution[i-1], best_node)  
                        + problem.cost(best_node, solution[i]) 
                        - problem.cost(solution[i-1], solution[i]))
                if cost < best_cost:
                    best_index = i
                    best_cost = cost
            
        # Update the solution and the list of nodes
        solution.insert(best_index, best_node)
        nodes.remove(best_node)
            
    return solution, problem.evaluate(solution)
