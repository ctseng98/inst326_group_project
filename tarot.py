import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from playsound import playsound


class Tarot:
    def __init__(self):
        """
        Initializes a set tarot cards by reading a csv file that contains a list of tarot cards.
        Args:
            tarot (set): A dictionary with the name of each tarot card as values.
        """
        self.tarot = pd.read_csv("T.csv")

    def pairing(self, number):
        """Pairs the number from Number class to a corresponding tarot card
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            A tarot card.
        """
        self.number = number
        select_card = self.tarot.iloc[self.number].to_dict()

        
        return select_card

    def image(self, number):
        """Pairs the number from Number class to a corresponding tarot card and lead to a link displying the card image
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            
        """
        self.number = number
        
        name = self.pairing(self.number).get("Name")
        url = self.pairing(self.number).get("Url")
        if name.startswith("The"):

            html = urlopen("{url}")
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find("img", {"src": re.compile("/images/tarotcards/")})
            new_url = images["src"]
            webbrowser.open(f"https://www.tarotcardmeanings.net{new_url}")
        elif name.endswith("Wands"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-wands-")})
            for image in images:
                url.append(image["src"])
            first_word = name.endswith("Wands").split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(url[int(corrspoding_num) - 1])

        elif name.endswith("Swords"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-swords-")})
            for image in images:
                url.append(image["src"])
            first_word = name.endswith("Swords").split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[int(corrspoding_num) - 1]
            )

        elif name.endswith("Cups"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-cups-")})
            for image in images:
                url.append(image["src"])
            first_word = name.endswith("Cups").split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[int(corrspoding_num) - 1]
            )

        elif name.endswith("Pentacles"):
            url = list()
            html = urlopen(
                "https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm"
            )
            bs = BeautifulSoup(html, "html.parser")
            images = bs.find_all("img", {"src": re.compile("/tarot-pentacles-")})
            for image in images:
                url.append(image["src"])
            first_word = name.endswith("Pentacles").split()[0]
            corrspoding_num = self.num(first_word)
            webbrowser.open(
                "https://www.tarotcardmeanings.net/" + url[int(corrspoding_num) - 1]
            )

    def num(self, label):
        """Pairs the label of tarots card and return the corresponding number
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