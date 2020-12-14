import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import random
from collections import Counter


class Number:
    """This class takes care of the translation from input digits o corrsponding tarot card."""

    def __init__(self, number=-1, sentence=""):
        """Initializes the input number and sentence
        modulus_stat (dict): A set that counts how many people got the same number from method translator()
        """
        if number != -1:
            self.number = number
            self.sentence = sentence
        else:
            self.sentence = sentence.lower()
            self.number = number
        self.modulus_count = Counter()
        self.alphabet_array = np.array([])
        self.alphabet_count = Counter()
        # print(self.sentence)

    def translator(self, number):
        """This method takes the 4 digit number and generates a corresponding number that hashes to a particular tarot card.
        Args:
            number (str): the number that the user inputs
        Returns:
            An integer that links to a tarot card.
            A png file of a pattern that is created by the input 4-digit number.
        Raises:
            ValueError: If user inputs alphabetical letters or not enough digits.
        """
        df_meaning = pd.read_csv("meaning.csv")
        df_color = pd.read_csv("color.csv")
        df_color = df_color.sample(frac=1).reset_index(drop=True)
        new_df = pd.merge(df_meaning, df_color, how="left", on="id").reset_index(
            drop=True
        )
        print(len(new_df))
        new_df = new_df[
            [
                "label",
                "English",
                "HEX",
                "description",
                "description_endroit",
                "description_envers",
            ]
        ]
        trans = (random.randint(0, 1000) * int(number)) % 78
        t = np.linspace(0, 2 * math.pi, 400)
        x = 16 * (np.sin(t) ** 3)
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        plt.plot(x, y)
        your_color_code = new_df.iat[trans, 2]
        your_color_name = new_df.iat[trans, 1]
        your_meaning = new_df.iloc[[trans], [0, 3, 4, 5]]
        print(trans)
        plt.fill_between(x, y, color=str(your_color_code))
        plt.savefig("your_color.png")
        print(f"Your signature color is {your_color_name}")
        print(your_meaning.T)
        # plt.show()
        # plt.close()
        return trans

    def generator(self):
        """Generates a random 4 digit number based on the sentence that the user put in. (Use regex)
        Args:
            sentence (str): A sentence that has a minimum of 4 characters and maximum of 20 characters.
        Returns:
            A string of integers.
        """
        # print(type(self.modulus_count))
        tem = [i for i in self.sentence if i != " " and i.isalpha()]
        # print(tem)
        self.alphabet_count.update(tem)
        most_com = self.alphabet_count.most_common(1)[0][0]
        output = self.translator(ord(most_com))

        return int(output)

    def stat(self):
        """Returns the stat of previous users.
        Args:
            hash (int)
        Returns:
            A histogram (?)
        """
        url_num = self.generator()
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
        plt.savefig("letter_frequency.png")
        # plt.show()
        return url_num