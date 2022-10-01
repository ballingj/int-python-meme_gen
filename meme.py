"""Commandline script to generate a meme.

The `generate_meme` function instantiate a MeMeGenerator instance
and calls the make_meme method of that instance to generate a meme.

The `if __name__ == "__main__` section parses three optional arguments:
picture directory, body, and author. If no arguments are passed, then,
the generator will pick from random pictures, as well as random quotes
and author.
"""
from fileinput import filename
import os
import random
import argparse

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    """Argument parser for the following CLI arguments."""
    parser = argparse.ArgumentParser(description='Create a random meme')
    parser.add_argument('--path', type=str, default=None,
                        help="path to an image file")
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image')

    args = parser.parse_args()
    print(args.path, args.body, args.author)

    print(generate_meme(args.path, args.body, args.author))
