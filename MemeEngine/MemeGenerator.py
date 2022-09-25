"""
Required:  
pip install Pillow
"""

from PIL import Image, ImageDraw, ImageFont
from random import randint


class MemeGenerator:
    
    def __init__(self, output_dir):
        """Instantiate MemeGenerator."""
        self.output_dir = output_dir
    
    def make_meme(self, img_path: str, text: str, 
                    author: str, width: int = 500) -> str: #generated image path
        """
        Create a Meme With a quote and suthor

        Arguments:
            img_path {str} - - the file location for the input image.
            text {str} - - the body of he quote.
            author {str} - - the author of the quote.
            width {int} - - The pixel width value. Default = 500.
        Returns:
            str - - the file path to the output image.
        """

        quote = f'''
        {text}
           - {author}
        '''
        
        with Image.open(img_path) as img:
            quote_pos = (randint(0, int(img.size[0]*0.6)), 
            randint(0, int(img.size[1]*0.8)))
            print(quote_pos, 'quote_pos')
            print(width, "<=width")
            if img.size[0] > 500:
                ratio = width/float(img.size[0])
                print(img.size, '<=  img size')  # debug line
                height = int(ratio*float(img.size[1]))
                img = img.resize((width, height), Image.NEAREST)
                print(img.size, '< =  final size')  # debug line

            if quote is not None:
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype('./fonts/LilitaOne-Regular.ttf', size=20)
                draw.text(quote_pos, quote, font=font, fill='white', 
                            stroke_fill='black', stroke_width=2)

        new_img = f'{randint(0,10000)}.jpg'
        out_path = f'{self.output_dir}/{new_img}'
        img.save(out_path)
        return out_path
