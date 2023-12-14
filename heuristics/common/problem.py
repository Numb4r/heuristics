from abc import ABC, abstractmethod


class Problem(ABC):
    """Abstract class for problem definition.
    """

    def __init__(self):
        pass


    @abstractmethod
    def evaluate(
        self, 
        solution: object
    ) -> int | float:
        """Computes the value of objective function for the given solution.
        
        :param solution: The solution to evaluate.
        :return: The value of objective function for the given solution.
        """
        raise NotImplementedError
    

    @abstractmethod
    def is_valid(
        self, 
        solution: object
    ) -> bool:
        """Checks if the given solution is valid.
        
        :param solution: The solution to check.
        :return: True if the given solution is valid, False otherwise.
        """
        raise NotImplementedError
