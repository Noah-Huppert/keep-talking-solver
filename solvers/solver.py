class Solver:
    """ Abstract class for loading and running module solvers
    """

    def solve(self):
        """ Logic for solving the module
        """
        raise NotImplementedError

    def man_version(self) -> str:
        """ Returns the bomb defusal manual version the solver is for
        """
        raise NotImplementedError

    def __str__(self) -> str:
        """ Returns the name of the module the solver solves
        """
        raise NotImplementedError
