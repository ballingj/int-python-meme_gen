from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .TxtIngestor import TxtIngestor


class Ingestor(IngestorInterface):
    Ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for Ingestor in cls.Ingestors:
            if Ingestor.can_ingest(path):
                return Ingestor.parse(path)
