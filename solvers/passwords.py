from typing import Set
from .solver import Solver

class PasswordsSolver(Solver):
    """ All possible passwords
    """
    possible_words = {"about","every","large","plant","spell","these","where","after","first",
             "learn","point","still","thing","which","again","found","never","right",
             "study","think","world","below","great","other","small","their","three",
             "would","could","house","place","sound","there","water","write"}

    def get_column(self, col: str):
        """ Prompts the user for a column of letters from the combination 
        display.

        Args:
            - col: Name of column to enter
        """
        in_letters = input("Enter column {}: ".format(col))

        letters = set()

        for in_letter in in_letters:
            letters.add(in_letter)

        return letters

    def match_words(self, words: Set[str], pos: int, col: Set[str]):
        """ Eliminates words if the letter in the provided position is not 
        in the column entered by the user.

        Args:
            - words: Set of words to check and eliminate from
            - pos: Index of letter to check in each word, starts at 0
            - col: Set of letters which must be in specified position in word
        """
        possible = set()

        for word in words:
            if word[pos] in col:
                possible.add(word)

        return possible

    def solve(self):
        # Get columns
        first_col = self.get_column("first")
        second_col = self.get_column("second")
        third_col = self.get_column("third")
        fourth_col = self.get_column("fourth")
        fifth_col = self.get_column("fifth")

        # Eliminate words
        guess_words = self.match_words(self.possible_words, 0, first_col)
        guess_words = self.match_words(guess_words, 1, second_col)
        guess_words = self.match_words(guess_words, 2, third_col)
        guess_words = self.match_words(guess_words, 3, fourth_col)
        guess_words = self.match_words(guess_words, 4, fifth_col)

        print()

        # Show result
        if len(guess_words) > 1:
            print("Solver failed: more than one possible password: {}".format(guess_words))
            return

        print("Password: {}".format(guess_words.pop()))

    def man_version(self):
        return "241"

    def __str__(self):
        return "Passwords"
