import argparse
import math
from threading import Thread
from random import Random
from heuristics import *


def solver_factory(heuristic, problem, rng):

    if heuristic == "random":
        return Thread(target=tsp.improved_random_heuristic, args=(problem, rng))
    
    if heuristic == "ils":
        x = tsp.improved_random_heuristic(problem, rng)
        ns = tsp.Switch()

        def ls(problem, solution, obj, rng):
            return ns.find_best(problem, solution, obj)
        
        def perturb(problem, solution, obj, rng):
            for _ in range(rng.randint(5, 11)):
                solution, obj = ns.find_any(problem, solution, obj, rng)
            return solution, obj
        
        return Thread(target=ils, kwargs={'problem': problem, 'rng': rng, 'local_search': ls, 'perturbation': perturb, 'initial_solution': x})


def main():
    """Main function that implements the command line interface for the module.
    """
    
    # Create the parser
    parser = argparse.ArgumentParser(prog='heuristics', description='Heuristics for the Traveling Salesman Problem.')
    parser.add_argument('--instance', dest='instance', type=str, required=True,
                        help='Path to the instance of the problem.')
    parser.add_argument('--heuristic', dest='heuristic',  type=str, required=True,
                        help='The heuristic used to solve the problem.')
    parser.add_argument('--seed', dest='seed', type=int, required=False, default=0,
                        help='Seed to initialize the pseudo-random number generator.')
    parser.add_argument('--time-limit', dest='time_limit', type=float, required=False, default=math.inf,
                        help='Time limit in seconds.')
    
    # Parse the arguments
    args = parser.parse_args()

    # Initialize the random number generator
    rng = Random(args.seed)

    # Load the instance of the problem
    problem = tsp.TSP(args.instance)

    # Solve the problem
    process = solver_factory(args.heuristic, problem, rng)
    process.daemon=True
    process.start()
    print(f'Timeout: {args.time_limit} seconds')
    process.join(timeout=args.time_limit)


if __name__ == '__main__':
    main()