import sys
import matplotlib
import numpy as np
from numpy import *
import matplotlib.pyplot as plt
import math

matplotlib.use("MacOSX")
plt.ion()
matplotlib.rcParams["interactive"] == True
import random
from collections import Counter
from argparse import ArgumentParser


from tarot import Tarot


class Number:
    """This class takes care of the translation from input digits o corrsponding tarot card."""

    def __init__(self, number=-1, sentence=""):
        """Initializes the input number and sentence
        modulus_stat (dict): A set that counts how many people got the same number from method translator()
        """
        if number != -1:
            self.number = int(number)
            self.sentence = sentence
        else:
            self.sentence = sentence.lower()
            self.number = number
        self.modulus_count = Counter()
        self.alphabet_array = np.array([])
        self.alphabet_count = Counter()
        # print(self.sentence)

    def translator(self):
        """This method takes the 4 digit number and generates a corresponding number that hashes to a particular tarot card.
        Args:
            number (str): the number that the user inputs
        Returns:
            An integer that links to a tarot card.
            A png file of a pattern that is created by the input 4-digit number.
        Raises:
            ValueError: If user inputs alphabetical letters or not enough digits.
        """
        trans = self.number % 78
        # print(number)
        # trans = number % 78
        self.modulus_count.update([trans])
        self.number = trans
        from matplotlib.patches import Ellipse

        NUM = 250

        ells = [
            Ellipse(
                xy=np.random.rand(2) * 10 * trans,
                width=np.random.rand(),
                height=np.random.rand(),
                angle=np.random.rand() * 50 * trans,
            )
            for i in range(NUM)
        ]

        fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
        for e in ells:
            ax.add_artist(e)
            e.set_clip_box(ax.bbox)
            e.set_alpha(np.random.rand())
            e.set_facecolor(np.random.rand(3))

        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        plt.savefig("figure.png")
        plt.show()
        return self.number

    def generator(self):
        """Generates a random 4 digit number based on the sentence that the user put in. (Use regex)
        Args:
            sentence (str): A sentence that has a minimum of 4 characters and maximum of 20 characters.
        Returns:
            A string of integers.
        """
        # print(type(self.modulus_count))
        tem = [i for i in self.sentence if i != " "]
        # print(tem)
        self.alphabet_count.update(tem)
        most_com = self.alphabet_count.most_common(1)[0][0]
        output = self.translator(random.randint(1, 300) * ord(most_com))
        self.number = int(output)

        return self.number

    def stat(self):
        """Returns the stat of previous users.
        Args:
            hash (int)
        Returns:
            A histogram (?)
        """
        self.generator()
        # print(self.alphabet_count)
        letters = np.array([i for i in self.alphabet_count.keys()])
        freq = np.array([i for i in self.alphabet_count.values()])
        x_bin = len(letters)
        # print(letters)
        # print(freq)
        f, ax = plt.subplots()
        plt.bar(letters, freq)
        plt.xticks(letters)
        plt.yticks(freq)
        plt.xlabel("Letters")
        plt.ylabel("Frequency")
        ax.set_xticks(range(0, x_bin))
        ax.set_xticklabels(letters)
        plt.savefig("figure.png")
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
    parser.add_argument("--number", default=-1, help="input number")
    parser.add_argument("--sentence", default="", help="input sentence")
    if parser is None:
        raise ValueError("Please input a sentence or a 4-digit number.")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.number:
        result_1 = Number(number=args.number)
        # print(result_1.translator())
        t_1 = Tarot(number=result_1.translator())
        t_1.image()
        result_1.translator()
    elif args.sentence:
        result_2 = Number(sentence=args.sentence)
        t_2 = Tarot(number=result_2.generator())
        t_2.image()
        result_2.stat()
