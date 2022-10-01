"""This class is derived from the abstract class IngestorInterface.

This class is used to parse a csv file containing a list of quotes
in the form `"When in doubt, go shoe-shopping",Mr. Paws`.
Setup: must install the following third party modules
pip install pandas.
"""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Parses a CSV File containing data."""

    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the csv file and return the list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
