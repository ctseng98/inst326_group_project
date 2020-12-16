import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser

from argparse import ArgumentParser
import sys
import feedparser


class Music:
    
    """ generates a video and automatically opens picture of tarot card in browser
    
    Attributes:
        url (set): url links to different videos
        tarot (int): a number that is between 0 and 14 that corresponds to a card
        feed: parses the url using feedparser  
        
    """
    
    
    def __init__(self, url, tarot):
        """Initializes a set of YouTube music by reading a csv file containing the urls.
        Args:
            urls (set): A set of urls that links to a YouTube music video.
            tarot (int): an number between 0 and 14
        """
        self.url = url
        self.feed = feedparser.parse(url)
        self.tarot = tarot
        pass

    def get_links(self):
        """Returns a list of string url
        Returns:
            A list of links to different videos
        """
        output = []
        for i in self.feed.entries:
            tem = [(i.title, j["href"]) for j in i.links if i.title not in output]
            output.append(tem[0][1])
        return output

    def play(self):
        """ automatically opens a browser with chosen card
        Returns:
            a browser with the chosen card from the tarot class
        Side Effects:
            opens web browser after you have run the code
        """
        dict_links = self.get_links()
        chosen_card_link = dict_links[self.tarot]
        webbrowser.open(
            chosen_card_link,
            new=2,
        )
