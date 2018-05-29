from .load import load_solvers
from .solvers import SOLVER_CLSS
from .choose import choose_solver

def run(print_fn=print, input_fn=input):
    """ Main loop for selecting and executing solvers
    Args:
        - print_fn: Function used to display information to users
        - input_fn: Function user to retrieve information from users
    """
    try:
        print_fn("Exit at any time by hitting Ctrl + c")
        print_fn()

        # Load solvers
        solvers = load_solvers(SOLVER_CLSS, print_fn=print_fn, input_fn=input_fn)
        if len(solvers) == 0:
            print_fn("No solvers, exiting")
            return

        print_fn()
 
        while True:
            solver = choose_solver(solvers, print_fn=print_fn, input_fn=input_fn)

            print_fn()
            print_fn("===== On the Subject of {} =====".format(solver))
            solver.solve()
            print_fn()
            print_fn("================================")
            print_fn()
    except KeyboardInterrupt:
        print_fn()
        print_fn("Exiting")
