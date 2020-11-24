import pandas as pd 
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
class Tarot:
    def __init__(self):
        """
        Initializes a set tarot cards by reading a csv file that contains a list of tarot cards.
        Args:
            tarot (set): A dictionary with the name of each tarot card as values. 
        """
        self.tarot = pd.read_csv('T.csv')
        
    def pairing(self, number):
        """Pairs the number from Number class to a corresponding tarot card
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            A tarot card.
        """
        self.number=number
        select_card=self.tarot.iloc[self.number].to_dict()
    
        # return print(f"{select_card.Name} \n--- Death Card: {select_card.Desc}\n--- Reversed Death Card: {select_card.Rdesc}")
        return select_card 
    def image(self,number):
        self.number=number
        # self.name=pairing(number).get('Name')
        name=pairing(self.number).get('Name')
        url=pairing(self.number).get('Url')
        if name.startswith('The'):
            
            html = urlopen('{url}')
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find('img', {'src':re.compile('/images/tarotcards/')})
            new_url=images['src']  
            webbrowser.open(f'https://www.tarotcardmeanings.net{new_url}')
        elif name.endswith('Wands'):
            url=list()
            html = urlopen('https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm')
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('/tarot-wands-')})
            for image in images: 
                url.append(image['src'])
            first_word=name.endswith('Wands').split()[0]    
            corrspoding_num=num(first_word)
            webbrowser.open(url[int(corrspoding_num)-1])
            
        
        elif name.endswith('Swords'):
            url=list()
            html = urlopen('https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm')
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('/tarot-swords-')})
            for image in images: 
                url.append(image['src'])
            first_word=name.endswith('Swords').split()[0]    
            corrspoding_num=num(first_word)
            webbrowser.open('https://www.tarotcardmeanings.net/'+url[int(corrspoding_num)-1])
        
        elif name.endswith('Cups'):
            url=list()
            html = urlopen('https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm')
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('/tarot-cups-')})
            for image in images: 
                url.append(image['src'])
            first_word=name.endswith('Cups').split()[0]    
            corrspoding_num=num(first_word)
            webbrowser.open('https://www.tarotcardmeanings.net/'+url[int(corrspoding_num)-1])
        
        elif name.endswith('Pentacles'):
            url=list()
            html = urlopen('https://www.tarotcardmeanings.net/minorarcana/tarot-wands.htm')
            bs = BeautifulSoup(html, 'html.parser')
            images = bs.find_all('img', {'src':re.compile('/tarot-pentacles-')})
            for image in images: 
                url.append(image['src'])
            first_word=name.endswith('Pentacles').split()[0]    
            corrspoding_num=num(first_word)
            webbrowser.open('https://www.tarotcardmeanings.net/'+url[int(corrspoding_num)-1])
            
            
    def num(self,label):
        self.label=label
        if label=='Ace':
            return 1
        elif label=='Two':
            return 2
        elif label=='Three':
            return 3
        elif label=='Four':
            return 4
        elif label=='Five':
            return 5
        elif label=='Six':
            return 6
        elif label=='Seven':
            return 7
        elif label=='Eight':
            return 8
        elif label=='Nine':
            return 9
        elif label=='Ten':
            return 10
        elif label=='Page':
            return 11   
        elif label=='Kight':
            return 12      
        elif label=='Queen':
            return 13
        elif label=='King':
            return 14
        
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
        

class Number:
    """This class takes care of the translation from input digits o corrsponding tarot card."""
    def __init__(self):
        """Initializes the input number"""
    def translator(self, number):
        """This method takes the 4 digit number and generates a corresponding number that links to a particular tarot card.
        Args:
            number (str): the number that the user inputs
        Returns:
            An integer that links to a tarot card.
        Raises:
            ValueError: If user inputs alphabetical letters or not enough digits.
        """
    def parse_args(arglist):
        """ Parses command-line arguments.

        The following optional command-line arguments are defined:

        -n / --number: the 4-digit number that the user chooses.
        
        Args:
            arglist (list of str): a list of command-line arguments.

        Returns:
            namespace: a string of a 4-digit integer.
        """
        