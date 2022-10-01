"""This class is derived from the abstract class IngestorInterface.

This class is used to parse a pdf file containing a list of quotes
in the form `"Treat yo self" - Fluffles`.
Setup: must install xpdf
Windows: download from https://www.xpdfreader.com/download.html
Linux: sudo apt-get install -y xpdf
Mac: brew install xpdf
"""
from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """This class is an instance of the abstract class IngestorInterface.

    Parses a PDF File containing data.
    """

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the pdf file and return the quotes."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        tmp = f'./tmp/{random.randint(0,100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        with open(tmp, "r") as file_ref:
            quotes = []

            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    new_quotes = QuoteModel(parse[0].strip('"'), parse[1])
                    quotes.append(new_quotes)

        os.remove(tmp)
        return quotes
