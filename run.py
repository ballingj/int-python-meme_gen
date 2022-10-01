# This is pre Encapsulation with Ingestor.py
# from QuoteEngine import DocxIngestor,
#                   CSVIngestor, PDFIngestor, TxtIngestor, Ingestor

# print(DocxIngestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
# print(CSVIngestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
# print(PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
# print(TxtIngestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))

# This is post encapsulation with Ingestor.py
from QuoteEngine import Ingestor

print(Ingestor.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))
print(Ingestor.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
print(Ingestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
print(Ingestor.parse('./_data/DogQuotes/DogQuotesTXT.txt'))
