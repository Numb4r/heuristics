import tsplib95
import matplotlib.pyplot as plt


class TSP:
    """Class that represents a TSP problem.
    """

    def __init__(self, filename: str):
        """Initializes the TSP problem from a file.

        This constructor loads a TSP problem data from a file in the TSPLIB format.

        :param filename: Path to the file containing the TSP problem data.
        """
        self.__data = tsplib95.load(filename)


    def size(self) -> int:
        """Return the number of nodes of the problem.

        :return: The number of nodes of the problem.
        """
        return self.__data.dimension
    

    def nodes(self) -> list[int]:
        """Return the list of nodes of the problem.

        Given n as the number of nodes in the instance, some instances from 
        TSPLIB may have nodes indexed from 1 to n, while others may have nodes 
        indexed from 0 to n-1. Then, this method returns a list with the nodes 
        of the problem, regardless of how they are indexed.

        :return: List of nodes of the problem.
        """
        return [i for i in self.__data.get_nodes()]
    

    def cost(self, i: int, j: int) -> float:
        """Return the cost of going from the node i to the node j.

        :param i: Start node.
        :param j: End node.
        :return: Cost of going from the node i to the node j.
        """
        return self.__data.get_weight(i, j)
    

    def evaluate(self, solution: list[int]) -> float:
        """Calculates the cost of a solution.

        :param solution: List of nodes that represents the solution.
        :return: Cost of the solution.
        """
        cost = 0
        for i in range(len(solution)):
            cost += self.cost(solution[i], solution[(i+1) % self.size()])
        return cost
    

    def is_valid(self, solution: list[int]) -> bool:
        """Checks if a solution is valid.

        :param solution: List of nodes that represents the solution.
        :return: True if the solution is valid, False otherwise.
        """
        return len(solution) == self.size() and set(solution) == set(self.nodes())
    

    def plot(self, solution: list[int], cost=None):
        """Plots the solution if the instance has coordinates.

        :param solution: List of nodes that represents the solution.
        :param cost: Cost of the solution.
        :raises Exception: If the instance does not have coordinates.
        """
        if self.__data.edge_weight_type not in ['EUC_2D', 'ATT']:
            raise Exception('This method can only be used with instances that have 2D-coordinates.')
        else:

            # Get node's coordinates
            coordinates = {i: tuple(self.__data.get_display(i)) for i in self.__data.get_nodes()}

            nodes_x = [coordinates[i][0] for i in self.__data.get_nodes()]
            nodes_y = [coordinates[i][1] for i in self.__data.get_nodes()]

            arcs_x = [coordinates[i][0] for i in solution] + [coordinates[solution[0]][0]]
            arcs_y = [coordinates[i][1] for i in solution] + [coordinates[solution[0]][1]]

            # Create (or activate) a figure
            plt.figure('tsp-tour', figsize=(7, 7), clear=True)
        
            # Draw the tour and nodes
            plt.plot(arcs_x, arcs_y, color='black', linestyle='-', linewidth=1, zorder=1)
            plt.scatter(nodes_x, nodes_y, s=90, zorder=2)

            # Show tour cost, if available
            if cost is not None:
                plt.gcf().text(0.15, 0.90, f'Cost: {cost}', fontsize=14)

            # Axis labels
            #plt.axis('off')
            plt.xticks([])
            plt.yticks([])
            plt.xlabel("x-coordinates", fontsize=14)
            plt.ylabel("y-coordinates", fontsize=14)

            # Show figure
            #plt.savefig('tsp-tour.png')
            plt.show()
