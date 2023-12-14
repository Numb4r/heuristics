import math
import time
import random
from collections.abc import Callable
from ..common import Problem


def simulated_annealing(
    problem: Problem,
    local_search: Callable[[Problem, object, int | float, random.Random], tuple[object, int | float]],
    start_temperature: float = 1,
    cooling_rate: float = 0.0005,
    k=10,
    rng: random.Random = random,
    cb: Callable[[int, object, int | float],
                 None] = lambda iter, solution, obj: None,
    threshold: float = 1e-6,
) -> tuple[object, int | float]:
    solution = problem.nodes()
    obj = problem.evaluate(solution)

    current_temperature = start_temperature
    best_solution = solution
    best_obj = obj
    it = 0
    solution, obj = local_search(problem, solution, obj, rng)

    while True:
        for _ in range(k):
            solution, obj = local_search(problem, solution, obj, rng)
            n = rng.random()
            acceptance = acceptance_probability(
                obj, best_obj, current_temperature)
            if obj < best_obj or n < acceptance:
                best_solution = solution
                best_obj = obj
                cb(it, best_solution, best_obj)

        current_temperature = cool_temperature(
            current_temperature, cooling_rate)

        if current_temperature < threshold:  # Reheat
            # print("reheat")
            current_temperature = start_temperature
        it += 1

    return best_solution, best_obj


def acceptance_probability(obj, best_obj, temperature):
    if obj < best_obj:
        return 1.0
    else:
        delta = (obj - best_obj) / (abs(best_obj) + 1e-6)
        return math.exp(-delta / temperature)


def cool_temperature(temperature, cooling_rate):
    return temperature * (1 - cooling_rate)
