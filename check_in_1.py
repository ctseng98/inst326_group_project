class Tarot:
    def __init__(self):
        """
        Initializes a set tarot cards by reading a csv file that contains a list of tarot cards.
        Args:
            tarot (set): A dictionary with the name of each tarot card as values. 
        """
    def pairing(self, number):
        """Pairs the number from Number class to a corresponding tarot card
        Args:
            number (int): the integer output from translator() in Number class.
        Returns:
            A tarot card.
        """

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
        