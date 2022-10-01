"""This class is derived from the abstract class IngestorInterface.

This class is used to select the appropriate Ingestor among the
different ingestors available based on the parsed file extension.
Choices: CSVIngestor, DocxIngestor, PDFIngestor, or TxtIngestor
returns: parsed quotes from the ingestor.
"""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    """This class is an instance of the abstract class IngestorInterface.

    Loops over the list of ingestors and parses the data if the file
    extension matches the parsed path.
    """

    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Iterate, find the appropriate ingestor, parse."""
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)
