import sys
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from argparse import ArgumentParser


class Number:
    """This class takes care of the translation from input digits o corrsponding tarot card."""

    def __init__(self, number=0, sentence=""):
        """Initializes the input number and sentence
        modulus_stat (dict): A set that counts how many people got the same number from method translator()
        """
        if number != 0:
            self.number = int(number)
        else:
            self.sentence = sentence.lower()
        self.modulus_count = Counter()
        self.alphabet_array = np.array([])

    def translator(self, number=0):
        """This method takes the 4 digit number and generates a corresponding number that hashes to a particular tarot card.
        Args:
            number (str): the number that the user inputs
        Returns:
            An integer that links to a tarot card.
        Raises:
            ValueError: If user inputs alphabetical letters or not enough digits.
        """
        trans = self.number % 78
        self.modulus_count({trans: 1})
        return trans

    def generator(self):
        """Generates a random 4 digit number based on the sentence that the user put in. (Use regex)
        Args:
            sentence (str): A sentence that has a minimum of 4 characters and maximum of 20 characters.
        Returns:
            A string of integers.
        """

        tem = [i for i in self.sentence]

        alphabet_count = Counter(tem)
        output = translator(alphabet_count.most_common())
        print(tem)
        print(alphabet_count)
        self.alphabet_array(tem)
        return output

    def stat(self):
        """Returns the stat of previous users.
        Args:
            hash (int)
        Returns:
            A histogram (?)
        """
        names = np.array(self.modulus_count.keys())
        freq = np.array(self.modulus_count.values())
        print(names)
        print(freq)
        plt.bar(names, freq)
        plt.xticks(self.modulus_count.keys())
        plt.yticks(self.modulus_count.values())
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        plt.show()


def parse_args(arglist):
    """Parses command-line arguments.

    The following optional command-line arguments are defined:

    -n / --number: the 4-digit number that the user chooses.
    -s / --sentence: A sentence with a maximum of 50 characters.
    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a string of a 4-digit integer.
    """
    parser = ArgumentParser()
    parser.add_argument("--number", default=0, help="input number")
    parser.add_argument("--sentence", default="", help="input sentence")
    if parser is None:
        raise ValueError("Please input a sentence or a 4-digit number.")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.number:
        Number(number=args.number)
    elif args.sentence:
        Number(sentence=args.sentence)
