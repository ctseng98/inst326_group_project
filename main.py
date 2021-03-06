from number import Number
from tarot import Tarot
from music import Music
from argparse import ArgumentParser
import sys


def parse_args(arglist):
    """Parses command-line arguments.

    The following optional command-line arguments are defined:

    -n / --number: the 4-digit number that the user chooses.
    -s / --sentence: A sentence with no maximum characters.
    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a string of a 4-digit integer.
    """
    parser = ArgumentParser()
    parser.add_argument("-n", "--number", default=-1, help="input number")
    parser.add_argument("-s", "--sentence", default="", help="input sentence")
    if parser is None:
        raise ValueError("Please input a sentence or a 4-digit number.")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    if args.number != -1:
        result_1 = Number(number=args.number)
        translated_num = result_1.translator(number=args.number)
        t_1 = Tarot(number=translated_num)
        t_1.image(number=translated_num)
        music = Music(
            url="https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
            tarot=translated_num,
        )
    else:
        result_2 = Number(sentence=args.sentence)
        url_num = result_2.stat()
        # print(url_num)
        t_2 = Tarot(number=url_num)
        t_2.image(number=url_num)
        music = Music(
            url="https://www.youtube.com/feeds/videos.xml?playlist_id=PLYyWwMzPI75TID--pLfPUJRjGIQJckSsL",
            tarot=url_num,
        )
    music.play()
