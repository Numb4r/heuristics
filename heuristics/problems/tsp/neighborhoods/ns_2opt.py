from itertools import chain
import random
from ..problem import TSP 
from ....common import Neighborhood
class TwoOpt(Neighborhood):
    """
    """
    def two_opt_switch_separeted(self,neighbor,i,j):
        return neighbor[:i],neighbor[i:j][::-1],neighbor[j:]
    def __init__(self):
        super()
    def find_best(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)

        best_i,best_j = None,None 
        best_delta = 0
        for i,_ in enumerate(solution):
            for j in range(i+2,len(solution)-1):
                
                delta =(problem.cost(solution[i],solution[(j+1)%len(neighbor)])+problem.cost(solution[j],solution[i-1])
                        -(problem.cost(solution[j],solution[(j+1)%len(neighbor)])+problem.cost(solution[i-1],solution[i])
                        ))
                if delta < best_delta:
                    best_i,best_j = i,j
                    best_delta = delta
        if best_i is not None and best_j is not None:
            neighbor = list(chain.from_iterable(self.two_opt_switch_separeted(neighbor,i,j)))
            neighbor_obj+=best_delta
        return neighbor,neighbor_obj
    def find_better(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)
        
        
        for i,_ in enumerate(solution):
            for j in range(i+2,len(solution)-1):
                
                delta =(problem.cost(solution[i],solution[(j+1)%len(neighbor)])+problem.cost(solution[j],solution[i-1])
                        -(problem.cost(solution[j],solution[(j+1)%len(neighbor)])+problem.cost(solution[i-1],solution[i])
                        ))
                if delta < -1e-6:
                    neighbor = list(chain.from_iterable(self.two_opt_switch_separeted(neighbor,i,j)))
                    neighbor_obj+=delta
                    return neighbor,neighbor_obj
        return neighbor,neighbor_obj
    def find_any(self, problem:TSP, solution:list[int], obj:float|None=None, rng:random.Random=random) -> tuple[list[int],float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)

        i = rng.randint(0, len(neighbor)-3)
        j = rng.randint(i+2, len(neighbor)-1)
        
        
        delta =(problem.cost(solution[i],solution[(j+1)%len(neighbor)])+problem.cost(solution[j],solution[i-1])
                        -(problem.cost(solution[j],solution[(j+1)%len(neighbor)])+problem.cost(solution[i-1],solution[i])
                        ))
        
        neighbor =  list(chain.from_iterable(self.two_opt_switch_separeted(neighbor,i,j)))
        neighbor_obj+=delta
        return neighbor,neighbor_obj
    


# i = 1
# j = 4
# [1, 2, 3, 4, 5, 6]
# [1] [4, 3, 2] [5, 6]
# [1, 4, 3, 2, 5, 6]


# i=0
# [1, 2, 3, 4, 5, 6]
# [] [4, 3, 2, 1] [5, 6]
# [4, 3, 2, 1, 5, 6]
