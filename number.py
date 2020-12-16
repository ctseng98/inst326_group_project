import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
import random
from collections import Counter


class Number:
    """This class takes care of the translation from input digits/sentence to
        the corrsponding tarot card.
    Attributes:
        number (int): A four-digit number input.
        sentence (str): A sentence input.
        test_mode (boolean): If the value is True, then the functions will
            omit any randomized proccess.
        alphabet_array (string array): An np array that stores the unique
            alphabet appeared in the sentence input.
        alphabet_count (dict): A counter object that keep tracks of the
            frequency of the alphabets appeared.
    """

    def __init__(self, number=-1, sentence="", test_mode=False):
        """Initializes the input number and sentence into lowercase letters.
        Args:
            alphabet_array (string array): An np array that stores the unique
                alphabet appeared in the sentence input.
            alphabet_count (dict): A counter object that keep tracks of the
                frequency of the alphabets appeared.
        Raises:
            Value Error: If the input sentence does not contain any letter.
        """

        if number != -1:
            self.sentence = sentence
        else:
            has_alpha = False
            for i in sentence:
                if i.isalpha():
                    has_alpha = True
            if not has_alpha:
                raise ValueError(
                    "Please input a sentence that contains letters or a 4 digit number."
                )
            else:
                self.sentence = sentence.lower()
        self.test_mode = test_mode  # For testing purposes
        self.number = number
        self.alphabet_array = np.array([])
        self.alphabet_count = Counter()
        # print(self.sentence)

    def meaning_color_tb(self):
        """Random sample color.csv and left join meaning.csv with color.csv
            according to their id.
        Returns:
            new_df (DataFrame): A new dataframe that only contains the
                colummns label, Englsih, HEX, description,
            description_endroit, description_envers.
        Note:
            The return value should have 78 rows.
            For testing purposes, if self.test_mode = True, then
                the function won't take a random sample.
        """
        df_meaning = pd.read_csv("meaning.csv")
        df_color = pd.read_csv("color.csv")
        if self.test_mode == False:
            df_color = df_color.sample(frac=1).reset_index(drop=True)

        new_df = pd.merge(df_meaning, df_color, how="left", on="id").reset_index(
            drop=True
        )
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
        return new_df

    def translator(self, number):
        """This method takes in the 4 digit number and generates a corresponding
            number that hashes to a particular tarot card.
        Args:
            number (int): The number that the user inputs
            boo (boolean): For testing purposes, I need to be able to predict
                the output number (i.e. trans), so if boo
            is True, the random.randint(0, 1000) would be taken out.
        Returns:
            trans (int): An integer of modulo 78 that links to a tarot card.
        Side effect:
            your_color (png): A png file saved in the working directory of a
                heart shape that is colored with your signature color.
        """
        new_df = self.meaning_color_tb()
        if self.test_mode == True:
            trans = int(number) % 78
        else:
            trans = (random.randint(0, 1000) * int(number)) % 78

        t = np.linspace(0, 2 * math.pi, 400)
        x = 16 * (np.sin(t) ** 3)
        y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
        plt.plot(x, y)
        your_color_code = new_df.iat[trans, 2]
        your_color_name = new_df.iat[trans, 1]
        your_meaning = new_df.iloc[[trans], [0, 3, 4, 5]]
        # print(trans)
        plt.fill_between(x, y, color=str(your_color_code))
        plt.savefig("your_color.png")
        print(f"Your signature color is {your_color_name}")
        print(your_meaning.T)
        # plt.show()
        # plt.close()
        return trans

    def generator(self):
        """Generates a random 4 digit number based on the sentence that the user
            put in by identifying the ASCII
        code of the most common letter.
        Returns:
            output (int): An integer (e.g. 97 for 'a') of the most common letter
                in the input sentence.
        Note:
            This function disregards any non-alphabet character
                (i.e. no spaces, puncuations, etc.).

        """
        tem = [i for i in self.sentence if i != " " and i.isalpha()]
        self.alphabet_count.update(tem)

        tem_dict = sorted(
            self.alphabet_count.items(), key=lambda x: (x[1], x[0]), reverse=True
        )
        # print(tem_dict)
        most_com = tem_dict[0][0]

        output = self.translator(ord(most_com))

        return int(output)

    def stat(self):
        """Creates a histogram that shows the frequency of each letter in the
            input sentence.
        Returns:
            url_num (int): A number that is later passed into the Music class
                to retrieve the associated YouTube link.
        Side effect:
            letter_frequency (png): A histogram plot saved in the working
                directory of the frequency of each alphabet appeared in
                the input sentence.
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