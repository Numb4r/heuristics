import math
import random
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..common import Problem


def thread_function(solution: list,
                    best_solution: list,
                    problem: Problem,
                    obj: float,
                    best_obj: float,
                    local_search: Callable[[Problem, object, int | float, random.Random], tuple[object, int | float]],
                    k: int,
                    current_temperature: float,
                    it: int,
                    cb: Callable[[int, object, int | float],
                                 None] = lambda iter, solution, obj: None,
                    rng: random = random.Random):
    for _ in range(k):
        solution, obj = local_search(problem, solution, obj, rng)
        acceptance = acceptance_probability(
            obj, best_obj, current_temperature)
        n = rng.random()
        if obj < best_obj or n < acceptance:
            best_solution = solution
            best_obj = obj
            cb(it, best_solution, best_obj)
    return (solution, obj, best_solution, best_obj)


def MT_simmulated_annealing(
    problem: Problem,
    local_search: Callable[[Problem, object, int | float, random.Random], tuple[object, int | float]],
    k=10,
    start_temperature: float = 100000,
    cooling_rate: float = 0.95,
    rng: random.Random = random,
    cb: Callable[[int, object, int | float],
                 None] = lambda iter, solution, obj: None,
    threshold: float = 1e-6,
    n_threads: int = 2
) -> tuple[object, int | float]:
    solution = problem.nodes()
    obj = problem.evaluate(solution)

    current_temperature = start_temperature
    best_solution = solution
    best_obj = obj
    solution, obj = local_search(problem, solution, obj, rng)
    threads = list()
    it = 0
    while True:
        with ThreadPoolExecutor(max_workers=n_threads) as executer:
            threads_result = [executer.submit(
                thread_function, solution, best_solution, problem, obj, best_obj, local_search, k, current_temperature, it, cb, rng) for _ in range(n_threads)]
            for future in as_completed(threads_result):
                solution, obj, best_s, best_o = future.result()
                if best_o < best_obj:
                    best_obj = best_o
                    best_solution = best_s

        current_temperature = cool_temperature(
            current_temperature, cooling_rate)

        if current_temperature < threshold:  # Reheat
            # print("reheat")
            current_temperature = start_temperature
        it += 1
    return best_solution, best_obj


"""

    # We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
"""

# for index in range(n_threads):
#     x = threading.Thread(target=thread_function, args=(index,solution,problem,rng,ta_solution,ta_obj))
#     threads.append(x)
#     x.start()


def acceptance_probability(obj, best_obj, temperature):
    if obj < best_obj:
        return 1.0
    else:
        delta = (obj - best_obj) / (abs(best_obj) + 1e-6)
        return math.exp(-delta / temperature)


def cool_temperature(temperature, cooling_rate):
    return temperature * (1 - cooling_rate)
