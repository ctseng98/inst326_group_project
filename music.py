import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser

from argparse import ArgumentParser
import sys
import feedparser


class Music:

    """Generates a video and automatically opens picture of tarot card in browser

    Attributes:
        url (str): url links to different videos
        tarot (int): a number that is between 0 and 14 that corresponds to a card
            (since YouTube only allows scraping at most 15 videos)
        feed (list): parses the url using feedparser

    """

    def __init__(self, url, tarot):
        """Initializes a set of YouTube music by reading a csv file containing the urls.
        Args:
            urls (str): A set of urls that links to a YouTube music video.
            tarot (int): an number between 0 and 14
        """
        self.url = url
        self.feed = feedparser.parse(url)
        self.tarot = tarot % 15
        pass

    def get_links(self):
        """Returns a list of string url
        Returns:
            output (str): A list of links to different videos
        """
        output = []
        for i in self.feed.entries:
            tem = [(i.title, j["href"]) for j in i.links if i.title not in output]
            output.append(tem[0][1])
        return output

    def play(self):
        """automatically opens a browser with chosen card
        Returns:
            a browser with the chosen card from the tarot class
            chosen_card_link -- str, corrsponding link for a specific tarot card
        Side Effects:
            opens web browser after you have run the code
        """
        dict_links = self.get_links()
        chosen_card_link = dict_links[self.tarot]
        webbrowser.open(
            chosen_card_link,
            new=2,
        )
        return chosen_card_link
