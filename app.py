"""Flask script for the Meme Generator webpage.

The `setup` function prepares the app by loading all the
random images and quotes available.

The `meme_rand` function generates a random meme when the
user presses the random button.

The `meme_form` function loads the form to input the custom
values if the user chooses to make a custom meme.

The `meme_post` function creates a user defined meme based
on the values presented in the form.
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator

app = Flask(__name__)

meme = MemeGenerator('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    # find all images within the images images_path directory
    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # select a random image from imgs array
    img = random.choice(imgs)
    # select a random quote from the quotes array
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    image_url = request.form.get('image_url')  # image url from the form
    body = request.form.get('body')  # grab body from the form
    author = request.form.get('author')  # grab author from the form

    try:
        user_img = requests.get(image_url)
    except requests.exceptions.ConnectionError as e:
        print("ConnectionError due to invalid URL.")
        return render_template('meme_error.html')
    except requests.exceptions.MissingSchema as e:
        print("Missing value in the Image URL.")
        return render_template('meme_error.html')
    else:
        temp_img = f'./tmp/{random.randint(0,10000)}.jpg'
        with open(temp_img, 'wb') as img:
            img.write(user_img.content)

        path = meme.make_meme(temp_img, body, author)
        os.remove(temp_img)

        return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
