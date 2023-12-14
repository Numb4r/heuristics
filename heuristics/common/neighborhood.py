import random
from abc import ABC, abstractmethod
from .problem import Problem


class Neighborhood(ABC):
    """Abstract class for neighborhood definition.
    """

    def __init__(self):
        pass


    @abstractmethod
    def find_best(
        self, 
        problem: Problem, 
        solution: object, 
        obj: int | float | None=None
    ) -> tuple[object, int | float]:
        """Returns the best neighbor of the given solution.
        
        :param problem: The problem for which the neighborhood is defined.
        :param solution: The reference solution for neighborhood construction.
        :param obj: The value of objective function for the initial solution (optional).
        :return: A tuple containing the solution found and its objective function value.
        """
        raise NotImplementedError
    

    @abstractmethod
    def find_better(
        self, 
        problem: Problem, 
        solution: object, 
        obj: int | float | None=None
    ) -> tuple[object, int | float]:
        """Returns a neighbor of the given solution that is better than it.
        
        :param problem: The problem for which the neighborhood is defined.
        :param solution: The reference solution for neighborhood construction.
        :param obj: The value of objective function for the initial solution (optional).
        :return: A tuple containing the solution found and its objective function value.
        """
        raise NotImplementedError
    

    @abstractmethod
    def find_any(
        self, 
        problem: Problem, 
        solution: object, 
        obj: int | float | None=None, 
        rng: random.Random=random
    ) -> tuple[object, int | float]:
        """Returns a neighbor of the given solution.
        
        :param problem: The problem for which the neighborhood is defined.
        :param solution: The reference solution for neighborhood construction.
        :param obj: The value of objective function for the initial solution (optional).
        :param rng: The random number generator (optional, default is to use the random module).
        :return: A tuple containing the solution found and its objective function value.
        """
        raise NotImplementedError
