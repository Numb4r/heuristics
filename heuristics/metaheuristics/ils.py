import math
import time
import random
from collections.abc import Callable
from ..common import Problem


def ils(
    problem: Problem,
    local_search: Callable[[Problem,object,int|float,random.Random], tuple[object,int|float]],
    perturbation: Callable[[Problem,object,int|float,random.Random], tuple[object,int|float]],
    start_solution: object,
    start_obj: int|float|None=None,
    max_iter: float=math.inf,
    max_iter_no_improv: float=math.inf,
    max_time: float=math.inf,
    rng: random.Random=random,
    eps: float=1e-6,
    cb: Callable[[int,object,int|float],None]=lambda iter, solution, obj: None
) -> tuple[object,int|float]:
    """Iterated Local Search algorithm.

    :param problem: The problem to solve.
    :param local_search: The local method.
    :param perturbation: The perturbation method.
    :param start_solution: The initial solution.
    :param start_obj: The value of objective function for the initial solution (optional).
    :param rng: The random number generator (optional, default is to use the random module).
    :param eps: The precision used for comparing objective function values (default is 1e-6).
    :param max_iter: The maximum number of iterations (default is 100).
    :param max_iter_no_improv: The maximum number of iterations without improvement (default is 25).
    :param max_time: Time limit in seconds (optional, default is math.inf).
    :param cb: A callback function that is called after each iteration (optional).
    :return: A tuple containing the best solution found and its objective function value.
    """

    # Start iteration counter and timer
    iter = 0
    iter_no_improv = 0
    start_time = time.time()

    # Find a local optimum from the initial solution
    best_solution, best_obj = local_search(problem, start_solution, start_obj, rng)

    # Call the callback function
    cb(0, best_solution, best_obj)

    while iter < max_iter and iter_no_improv < max_iter_no_improv and time.time() - start_time < max_time:

        # Increment iteration counter
        iter += 1

        # Perturbate the current solution
        solution, obj = perturbation(problem, best_solution, best_obj, rng)
        

        # Find a local optimum from the perturbated solution
        solution, obj = local_search(problem, solution, obj, rng)

        # Update the best solution
        if obj + eps < best_obj:
            best_solution = solution
            best_obj = obj
            iter_no_improv = 0
        else:
            iter_no_improv += 1

        # Call the callback function
        cb(iter, best_solution, best_obj)

    # Return the best solution found
    return best_solution, best_obj
