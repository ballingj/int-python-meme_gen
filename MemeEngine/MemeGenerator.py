"""Meme generator class.

This module takes in an image and a quote to generate a meme
using a third party module Pillow.

setup:
pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
from random import randint
import textwrap


def test_quote_len(quote: str, img_size: int):
    """Qustomize position of text depending on size."""
    if len(quote) <= 120:
        quote_pos = (randint(0, int(img_size*0.45)),
                     randint(0, int(img_size*0.8)))
        return quote_pos
    if len(quote) >= 120 and len(quote) < 200:
        quote_pos = (randint(0, int(img_size*0.3)),
                     randint(0, int(img_size*0.5)))
        return quote_pos
    if len(quote) >= 200:
        return (10, 10)


def quote_wrapper(text: str, author: str):
    """Wrap long quotes into multiple lines."""
    print(len(text), "text length")
    quote_wrap = textwrap.TextWrapper(width=35)
    text = quote_wrap.fill(text=text)
    quote = f'''
    {text}
        - {author}'''
    print(len(quote), "quote length")
    return quote


def img_resize(img, width):
    """Resize the image if greater than 500 width."""
    print(img.size, '<=  img original size')  # debug line
    if img.size[0] > 500:
        ratio = width/float(img.size[0])
        height = int(ratio*float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)
        print(img.size, '<=  img resize')  # debug line
        return img
    else:
        print(img.size, '<=  img size')  # debug line
        return img


def draw_meme(img, quote, quote_pos):
    """Draw the meme."""
    if quote is not None:
        if len(quote) >= 300:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                      size=20)
            draw.text(quote_pos, "You quote is too long; please choose /"
                      "a shorter quote.", font=font, fill='red',
                      stroke_fill='black', stroke_width=2)
        else:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf',
                                      size=20)
            draw.text(quote_pos, quote, font=font, fill='white',
                      stroke_fill='black', stroke_width=2)


class MemeGenerator:
    """Create a Meme With a quote and author.

    Arguments:
        img_path {str} - - the file location for the input image.
        text {str} - - the body of he quote.
        author {str} - - the author of the quote.
        width {int} - - The pixel width value. Default = 500.
    Returns:
        str - - the file path to the output image.
    """

    def __init__(self, output_dir):
        """Instantiate MemeGenerator."""
        self.output_dir = output_dir

    def make_meme(self, img_path: str, text: str,
                  author: str, width: int = 500) -> str:
        """Generate the meme blending the pic and text."""
        quote = quote_wrapper(text, author)

        # read the image file
        with Image.open(img_path) as img:
            resized_img = img_resize(img, width)
            print(width, "<=width")
            quote_pos = test_quote_len(quote, resized_img.size[0])
            print(quote_pos, '<=quote_pos')  # debug line
            draw_meme(resized_img, quote, quote_pos)

        # write the new file
        new_img = f'{randint(0,10000)}.jpg'
        out_path = f'{self.output_dir}/{new_img}'
        resized_img.save(out_path)
        return out_path
