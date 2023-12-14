from ..common import Problem
from ..common import Neighborhood


def first_improvement_local_search(
    problem: Problem, 
    neighborhood: Neighborhood, 
    solution: object, 
    obj: int | float | None=None, 
    eps: float=1e-6
) -> tuple[object, int | float]:
    """First improvement local search algorithm.

    :param problem: The problem for which the neighborhood is defined.
    :param neighborhood: The neighborhood.
    :param solution: The initial solution.
    :param obj: The value of objective function for the initial solution (optional).
    :param eps: The precision used for comparing objective function values (optional, default is 1e-6).
    :return: A tuple containing the best solution found and its value of objective function.
    """
    best_solution = solution
    best_obj = obj if obj is not None else problem.evaluate(solution)

    while True:
        neighbor, neighbor_obj = neighborhood.find_better(problem, best_solution, best_obj)
        if neighbor_obj + eps < best_obj:
            best_solution = neighbor
            best_obj = neighbor_obj
        else:
            break

    return best_solution, best_obj
