import random
from ..problem import TSP


def random_heuristic(problem: TSP, rng: random.Random=random) -> tuple[list[int], float]:
    """Randomly generates a solution for the TSP problem.

    :param problem: The TSP problem.
    :param rng: The random number generator (optional, default is to use the random module).
    :return: A random solution and its cost.
    """
    nodes = problem.nodes()
    rng.shuffle(nodes)
    return nodes, problem.evaluate(nodes)
