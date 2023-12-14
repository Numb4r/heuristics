import random
from ..common import Problem
from ..common import Neighborhood


def random_improvement_local_search(
    problem: Problem, 
    neighborhood: Neighborhood, 
    solution: object, 
    obj: int | float | None=None, 
    attempts_limit: int=100,
    rng: random.Random=random,
    eps: float=1e-6
) -> tuple[object, int | float]:
    """Best improvement local search algorithm.

    :param problem: The problem for which the neighborhood is defined.
    :param neighborhood: The neighborhood.
    :param solution: The initial solution.
    :param obj: The value of objective function for the initial solution.
    :param limit_attempts: The maximum number of unsuccessful attempts (optional, default is 100).
    :param rng: The random number generator (optional, default is to use the random module).
    :param eps: The precision used for comparing objective function values (optinal, default is 1e-6).
    :return: A tuple containing the best solution found and its objective function value.
    """
    best_solution = solution
    best_obj = obj if obj is not None else problem.evaluate(solution)

    unsuccessful_attempts = 0
    while unsuccessful_attempts < attempts_limit:
        neighbor, neighbor_obj = neighborhood.find_any(problem, best_solution, best_obj, rng)
        if neighbor_obj + eps < best_obj:
            best_solution = neighbor
            best_obj = neighbor_obj
            unsuccessful_attempts = 0
        else:
            unsuccessful_attempts += 1

    return best_solution, best_obj
