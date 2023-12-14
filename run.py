import sys
import math
import random
from threading import Thread

import heuristics.problems.tsp as tsp
import heuristics.local_search as ls
import heuristics.metaheuristics as mh
from heuristics.problems.tsp.neighborhoods.ns_shift import Shift


# -------------------------------------------------------------------
# -------------------------------------------------------------------

# Your code here!
def solver(problem, rng, cb):

    ns = [tsp.Switch(), tsp.Shift(), tsp.TwoOpt(), tsp.ThreeOpt()]

    def local_search_best(problem, solution, obj):
        return ls.best_improvement_local_search(problem, ns[0], solution, obj)

    def local_search_first(problem, solution, obj):
        return ls.first_improvement_local_search(problem, ns[0], solution, obj)

    def local_search_rand(problem, solution, obj, rng):
        return ls.random_improvement_local_search(problem, ns[0], solution, obj, rng=rng)

    def local_search_vnd(problem, solution, obj):
        return ls.vnd(problem, ns, solution, obj, False)

    # def create_rand_sol():
    #     return tsp.random_heuristic

    def perturbation(problem, solution, obj, rng):
        for _ in range(rng.randint(5, 10)):
            solution, obj = ns[0].find_any(problem, solution, obj, rng)
        return solution, obj

    # solution, obj = tsp.random_heuristic(problem, rng)
    # solution, obj = mh.ils(problem, local_search, perturbation, solution, obj, rng=rng, cb=cb)
    solution, obj = mh.multistart(
        problem, local_search_rand, local_search_first,  rng=rng, cb=cb)
    # solution, obj = mh.simulated_annealing(
    #     problem, local_search_rand, rng=rng, cb=cb)
    # solution, obj = mh.MT_simmulated_annealing(
    #     problem, local_search_rand, rng=rng, cb=cb, n_threads=2)

# Iteration 2059: 13084119
# Iteration 2059: 13084119
# -------------------------------------------------------------------
# -------------------------------------------------------------------


# Some globals
global problem, best_solution, best_obj
problem = None
best_obj = None
best_obj = math.inf

# Callback function


def cb(iter, solution, obj):
    global problem, best_solution, best_obj
    obj = problem.evaluate(solution)
    if obj + 1e-6 < best_obj:
        best_solution = solution
        best_obj = obj
        print(f'Iteration {iter}: {best_obj}')


# CLI arguments
instance = sys.argv[1]
seed = int(sys.argv[2])
timelimit = float(sys.argv[3])

# Initialize random number generator
rng = random.Random(seed)

# Load problem
problem = tsp.TSP(instance)

# # Solve problem
process = Thread(target=solver, args=(problem, rng, cb))
process.daemon = True
process.start()
process.join(timeout=timelimit)
