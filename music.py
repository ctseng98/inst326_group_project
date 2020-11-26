import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from playsound import playsound

class Music:
    def __init__(self):
        """Initializes a set of YouTube music by reading a csv file containing the urls.
        Args:
            urls (set): A set of urls that links to a YouTube music video.    
        """
        pass
    def url_generator(self, number):
        """Generates a YouTube link corrspoding to the tarod card number.
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            song title (str): the song title of the corrsponding url.
        """
    def play_song(self)
        """ automatically plays the song
        Returns:
            plays the music of the song that was generated. 
        """
        song_play = playsound(self.sound)
        return song_play
        
        

