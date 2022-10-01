"""This class is derived from the abstract class IngestorInterface.

This class is used to parse a simple txt file containing a list of
quotes in the form `To bork or not to bork - Bork`.
"""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TxtIngestor(IngestorInterface):
    """Parses a txt File containing data."""

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a txt file and return the list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as infile:
            content = infile.readlines()
            for line in content:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quote = QuoteModel(parse[0].strip('"'), parse[1])
                    quotes.append(new_quote)
        return quotes
