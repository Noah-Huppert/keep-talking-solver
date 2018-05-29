from typing import List
from .solver import Solver

def get_man_version(input_fn=input) -> str:
    """ Prompt the user for the manual version they are using.

    Args:
        - input_fn: Function used to prompt the user for input

    Returns: Manual version
    """
    return input_fn("Manual Verification Code: ")

def load_solvers(solver_clss: List[Solver], print_fn=print, input_fn=input) -> List[Solver]:
    """ Loads a list of solvers, ensuring the manual version provided by the 
    user matches the manual version for each of the solvers

    Args:
        - solver_clss: Possible solvers classes, not instances
        - print_fn: Function used to print output to users
        - input_fn: Function used to prompt users for input

    Returns: Compatible solvers
    """
    man_version = get_man_version(input_fn=input_fn)

    compatible = []

    for solver_cls in solver_clss:
        solver = solver_cls()
        solver_man_version = solver.man_version()

        if solver_man_version == man_version:
            compatible.append(solver)
        else:
            print_fn("{} solver not compatible with manual version, needs manual version {}".format(solver, solver_man_version))

    return compatible
