"""This is the abstract class model for different ingestors.

The ingestors derived from this ABC are CSVIngestor, DocxIngestor,
PDFIngestor, TxtIngestor, and Ingestor.
"""
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

from typing import List


class IngestorInterface(ABC):
    """Abstract base class for the ingestors instances."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if file ext is in the allowed ext list."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract parse method meant to be overwritten."""
        pass
