"""This class is derived from the abstract class IngestorInterface.

This class is used to parse a docx file containing a list of quotes
in the form `"Bark like no one’s listening" - Rex`.
Setup: must install the following third party modules
pip install -U setuptoold
pip install python-docx
"""
from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """This class is an instance of the abstract class IngestorInterface.

    Parses a DOCX File containing data.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the docx file and return the list of quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                # print(para.text)
                parse = para.text.split(' - ')
                # print(parse)
                new_quote = QuoteModel(parse[0].strip('"'), parse[1])
                quotes.append(new_quote)
        # print(quotes)
        return quotes
