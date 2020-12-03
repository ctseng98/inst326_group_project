import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from playsound import playsound
from argparse import ArgumentParser
import sys
import feedparser


class Music:
    def __init__(self):
        """Initializes a set of YouTube music by reading a csv file containing the urls.
        Args:
            urls (set): A set of urls that links to a YouTube music video.
        """
        self.url = url
        self.feed = feedparser.parse(url)

        pass

    def get_links(self):
        """Returns a list of tuples of the title and url if have type audio
        Returns:
            A list of tuples.
        """
        output = []
        for i in self.feed.entries:
            tem = [(i.title, j["href"]) for j in i.links if i.title not in output]
            output.append(tem[0])
        return output

    def play(self):
        """automatically plays the youtube video
        Returns:
            plays youtube video that was generated.
        """
        play_video = playsound(self.sound)
        return play_video


def main(url):
    """ Extract titles and links from an RSS feed. """
    fw = Music(url)
    l = fw.get_links()
    for title, link in fw.get_links():
        print(f"{title} | {link}")


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("url", help="url of the RSS feed of a podcast")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.url)
