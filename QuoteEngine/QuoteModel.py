"""This class is used to create an instance of quotes.

Quotes will be pulled from different sources, mostly from
different quote ingestors.  User also have an option to generate
a custom quote created from the App module or via commandline.
"""


class QuoteModel():
    """Model for quotes."""

    def __init__(self, body, author):
        """Instantiate the quote class."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Return the values of the instance."""
        return f'{self.body} - {self.author}'
