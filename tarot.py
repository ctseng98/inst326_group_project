import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
import sys

from argparse import ArgumentParser


class Tarot:
    def __init__(self, number):
        """
        Initializes a set tarot cards by reading a csv file that contains a list of tarot cards.
        Args:
            tarot (set): A dictionary with the name of each tarot card as values.
        """
        self.tarot = pd.read_csv("T.csv")
        self.number = number

    def pairing(self, number):
        """Pairs the number from Number class to a corresponding tarot card
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            A tarot card (str).
        """

        select_card = self.tarot.iloc[number].to_dict()

        return select_card

    def image(self, number):
        """Pairs the number from Number class to a corresponding tarot card and lead to a link displying the card image
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:

        """

        name = self.pairing(number).get("Name")
        url = self.pairing(number).get("Url")
        if name.startswith("The"):

            html = urlopen(url)
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find("img", {"src": re.compile("/images/tarotcards/")})
            new_url = images["src"]
            webbrowser.open(f"https://www.tarotcardmeanings.net{new_url}", new=2)
        elif name.endswith("Wands"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-wands-")})
            for image in images:
                url.append(image["src"])
            first_word = name.split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(url[corrspoding_num - 3], new=2)

        elif name.endswith("Swords"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-swords.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-swords-")})
            for image in images:
                url.append(image["src"])
            first_word = name.split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[corrspoding_num - 3],
                new=2,
            )

        elif name.endswith("Cups"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-cups.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-cups-")})
            for image in images:
                url.append(image["src"])
            first_word = name.split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[corrspoding_num - 3],
                new=2,
            )

        elif name.endswith("Pentacles"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-pentacles.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-pentacles-")})
            for image in images:
                url.append(image["src"])
            first_word = name.split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[corrspoding_num - 3],
                new=2,
            )

    def num(self, label):
        """Pairs the label of tarots card from the csv file and return the corresponding number
        Args:
            label (str): the label of tarots card
        Returns:
            corresponding number
        """
        self.label = label
        if label == "Ace":
            return 1
        elif label == "Two":
            return 2
        elif label == "Three":
            return 3
        elif label == "Four":
            return 4
        elif label == "Five":
            return 5
        elif label == "Six":
            return 6
        elif label == "Seven":
            return 7
        elif label == "Eight":
            return 8
        elif label == "Nine":
            return 9
        elif label == "Ten":
            return 10
        elif label == "Page":
            return 11
        elif label == "Kight":
            return 12
        elif label == "Queen":
            return 13
        elif label == "King":
            return 14
