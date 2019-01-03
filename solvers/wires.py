from .solver import Solver
from .choose import prompt_int

class WiresSolver(Solver):
    def solve(self):
        # Get number of wires
        num_wires = prompt_int(6, min_val=3, prompt_txt="Number of wires? ")

    def get_wire_order(self, num) -> str:
        """ Gets the wire order.
        
        Args:
            - num: Number of wires that must be in order

        Returns: String with wires in order
        """
        print("red = r, white = w, blue = b, bl)

    def man_version(self):
        return "241"

    def __str__(self):
        return "Wires"
