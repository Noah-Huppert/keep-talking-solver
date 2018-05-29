from typing import List
from .solver import Solver

def list_solver_options(solvers: List[Solver]) -> str:
    """ Returns a list of solvers which can be selected
    """
    out = "On the Subject of:\n\n"

    i = 1
    for solver in solvers:
        out += "    {}) {}".format(i, solver)
        i += 1

    return out

def prompt_int(max_val: int, min_val: int = 1, prompt_txt: str = "> ",
               print_fn=print, input_fn=input) -> int:
    """ Prompts the user for an integer in a range.

    Args:
        - max_val: Maximum accepted integer value
        - min_val: Minimum accepted integer value
        - prompt_txt: Text to display before prompting
        - print_fn: Function used to display output to user
        - input_fn: Function used to prompt the user for input

    Returns: Provided integer between values
    """
    val = None

    while (val is None) or (val < min_val) or (val > max_val):
        if val is not None:
            print_fn("Error: Input must be in the range [{}, {}]".format(
                min_val, max_val))

        try:
            val = int(input_fn(prompt_txt))
        except ValueError:
            print("Error: Input must be an integer")

    return val

def choose_solver(solvers: List[Solver], print_fn=print, input_fn=input) -> Solver:
    """ Asks the user which solver they would like to select.

    Args:
        - solvers: Possible solvers to select
        - print_fn: Function used to display output to user
        - input_fn: Function used to retrieve input from user

    Returns: Solver user selects
    """
    # List options
    print_fn(list_solver_options(solvers))
    print_fn()

    selected = prompt_int(len(solvers), print_fn=print_fn, input_fn=input_fn)

    return solvers[selected-1]
