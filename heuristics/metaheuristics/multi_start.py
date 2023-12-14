import math
import time
import random
from collections.abc import Callable
from ..common import Problem


def multistart(
    problem: Problem,
    random_start: Callable[[Problem, object, int | float, random.Random], tuple[object, int | float]],
    local_search: Callable[[Problem, object, int | float, random.Random], tuple[object, int | float]],
    k=10,
    rng: random.Random = random,
    cb: Callable[[int, object, int | float],
                 None] = lambda iter, solution, obj: None
) -> tuple[object, int | float]:

    solution = problem.nodes()
    obj = problem.evaluate(solution)
    itr = 0
    solution, obj = random_start(problem, solution, obj, rng)
    best_solution = solution
    best_obj = obj

    while True:
        # Gerar solucao aleatoria
        solution, obj = random_start(problem, solution, obj, rng)

        for _ in range(k):
            solution, obj = local_search(problem, solution, obj)
            if obj < best_obj:
                best_solution = solution
                best_obj = obj
                cb(itr, best_solution, best_obj)
        itr += 1
    return best_solution, best_obj
