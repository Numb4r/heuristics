import random
from ..problem import TSP
from ....common import Neighborhood


class Shift(Neighborhood):
    """Switch neighborhood for the TSP.
    """

    def __init__(self):
        super()

    def find_best(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        solution_best = solution 
        obj_best = obj

        for i,_ in enumerate(solution):
            node = solution[i]
            neighbor = solution.copy()
            neighbor.remove(node)
            for j in enumerate(neighbor):
                neighbor.insert(j,node)
                obj = problem.evaluate(neighbor)
                if obj < obj_best:
                    solution_best = neighbor.copy()
                    obj_best = obj
    
                neighbor.remove(node)
        return solution_best,obj_best
    def find_better(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        solution_best = solution 
        obj_best = obj

        for i,_ in enumerate(solution):
            node = solution[i]
            neighbor = solution.copy()
            neighbor.remove(node)
            for j in enumerate(neighbor):
                neighbor.insert(j,node)
                obj = problem.evaluate(neighbor)
                if obj < -1e-6:
                    solution_best = neighbor.copy()
                    obj_best = obj
    
                neighbor.remove(node)
        return solution_best,obj_best

    def find_any(self, problem:TSP, solution:list[int], obj:float|None=None, rng:random.Random=random) -> tuple[list[int],float]:
        neighbor = solution.copy()
        i = rng.randint(0,len(solution)-1)
        node = neighbor[i]
        neighbor.remove(node)
        j = rng.randint(0,len(solution)-1)
        neighbor.insert(j,node)
        obj = problem.evaluate(neighbor)
        return neighbor,obj
        