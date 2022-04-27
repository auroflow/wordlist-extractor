"""\
This file extracts words from an epub file.
"""
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
import io
import re
from zipfile import ZipFile


class DocumentParser(HTMLParser):
    def __init__(self, words: set[str]):
        HTMLParser.__init__(self)
        self.words = words

    def handle_data(self, data):
        new_words = {word.lower() for word in re.findall(r'\w+', data)}
        self.words.update(new_words)


def get_words(filename: str):
    """
    Get a list of words that appear in an epub file.

    Args:
        filename: The epub file.
    
    Returns:
        A list of words that appear in the epub file.
    """
    words: set[str] = set()

    ns = {
        'ns': 'urn:oasis:names:tc:opendocument:xmlns:container',
        'pkg': 'http://www.idpf.org/2007/opf'
    }

    with ZipFile(filename) as book:
        # Get the content.opf path from META-INF/container.xml
        meta_inf = book.read('META-INF/container.xml').decode('utf-8')
        root = ET.fromstring(meta_inf)

        content_opf_path = root.find(
            'ns:rootfiles/ns:rootfile', ns).get('full-path')

        # Get document list from content.opf
        content_opf = book.read(content_opf_path).decode('utf-8')
        root = ET.fromstring(content_opf)
        items = root.findall('pkg:manifest/pkg:item', ns)
        paths = []
        for item in items:
            if item.get('media-type') == 'application/xhtml+xml':
                paths.append(item.get('href'))

        # Parse each document
        for path in paths:
            doc = book.read(path).decode('utf-8')
            parser = DocumentParser(words)
            parser.feed(doc)

    return words
