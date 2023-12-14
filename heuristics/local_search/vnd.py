from ..common import Problem, Neighborhood


def vnd(
    problem: Problem,
    neighborhoods: list[Neighborhood],
    solution: object,
    obj: int | float | None=None,
    best_improvement: bool=False,
    eps: float=1e-6
) -> tuple[object, int | float]:
    """Variable Neighborhood Descent algorithm.
    
    :param problem: The problem for which the neighborhoods are defined.
    :param neighborhoods: The list of neighborhoods.
    :param solution: The initial solution.
    :param obj: The value of objective function for the initial solution (optional).
    :param best_improvement: Whether to use the best improvement strategy (optional, default is False).
    :param eps: The precision used for comparing objective function values (optional, default is 1e-6).
    :return: A tuple containing the best solution found and its value of objective function.
    """
    best_solution = solution
    best_obj = obj if obj is not None else problem.evaluate(best_solution)

    k = 0
    while k < len(neighborhoods):
            
        # Find a neighbor in the k-th neighborhood
        if best_improvement:
            neighbor, neighbor_obj = neighborhoods[k].find_best(problem, solution)
        else:
            neighbor, neighbor_obj = neighborhoods[k].find_better(problem, solution)

        # If the neighbor is better than the current solution, then move to the neighbor
        if neighbor_obj + eps < best_obj:
            best_solution = neighbor
            best_obj = neighbor_obj
            k = 0
        else:
            k += 1

    return best_solution, best_obj
