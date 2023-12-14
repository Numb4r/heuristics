from itertools import chain
import random
from ..problem import TSP 
from ....common import Neighborhood
class ThreeOpt(Neighborhood):
    """
    """
    def __init__(self):
        super()
    def three_opt_switch_separeted(self,neighbor,i,j,k):
        return neighbor[:i],neighbor[i:j][::-1],neighbor[j:k][::-1] ,neighbor[k:]
    def find_best(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)

        best_i,best_j,best_k = None,None 
        best_delta = 0
        for i,_ in enumerate(solution):
            for j in range(i+2,len(solution)-1):
                for k in range(j+2,len(solution)-1):
                    delta =(problem.cost(solution[i-1],solution[j-1])
                            +problem.cost(solution[i],solution[k-1])
                            +problem.cost(solution[j],solution[k%len(neighbor)])
                            -(
                            problem.cost(solution[i],solution[i-1])
                            -problem.cost(solution[j],solution[j-1])
                            -problem.cost(solution[k%len(neighbor)],solution[k-1])
                            ))
                    if delta < best_delta:
                        best_i,best_j,best_k = i,j,k
                        best_delta = delta
        if best_i is not None and best_j is not None:
            neighbor = list(chain.from_iterable(self.three_opt_switch_separeted(neighbor,best_i,best_j,best_k)))
            neighbor_obj+=best_delta
        return neighbor,neighbor_obj
    def find_better(self, problem:TSP, solution:list[int], obj:float|None=None) -> tuple[list,float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)
        
        best_delta = 0
        for i,_ in enumerate(solution):
            for j in range(i+2,len(solution)-1):
                for k in range(j+2,len(solution)-1):
                    delta =(problem.cost(solution[i-1],solution[j-1])
                            +problem.cost(solution[i],solution[k-1])
                            +problem.cost(solution[j],solution[k%len(neighbor)])
                            -(
                            problem.cost(solution[i],solution[i-1])
                            -problem.cost(solution[j],solution[j-1])
                            -problem.cost(solution[k%len(neighbor)],solution[k-1])
                            ))
                    if delta < -1e-6:
                        neighbor = list(chain.from_iterable(self.three_opt_switch_separeted(neighbor,i,j,k)))
                        neighbor_obj+=delta
                        return neighbor,neighbor_obj
        return neighbor,neighbor_obj
    def find_any(self, problem:TSP, solution:list[int], obj:float|None=None, rng:random.Random=random) -> tuple[list[int],float]:
        neighbor = solution.copy()
        neighbor_obj = obj if obj is not None else problem.evaluate(neighbor)

        i = rng.randint(0, len(neighbor)-3)
        j = rng.randint(i+2, len(neighbor)-1)
        print(j+2,len(neighbor))
        k = rng.randint(j+1,len(neighbor)-1) # TODO: Arrumar isso
        
        delta =(problem.cost(solution[i-1],solution[j-1])
                            +problem.cost(solution[i],solution[k-1])
                            +problem.cost(solution[j],solution[k%len(neighbor)])
                            -(
                            problem.cost(solution[i],solution[i-1])
                            -problem.cost(solution[j],solution[j-1])
                            -problem.cost(solution[k%len(neighbor)],solution[k-1])
                            ))
        
        neighbor =  list(chain.from_iterable(self.three_opt_switch_separeted(neighbor,i,j,k)))
        neighbor_obj+=delta
        return neighbor,neighbor_obj
    
