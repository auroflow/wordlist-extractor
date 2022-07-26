import xml.etree.ElementTree as ET
from zipfile import ZipFile
from . import TextExtractor


class EpubTextExtractor(TextExtractor):
    """\
    This file extracts texts from an epub file.
    """

    def get_text(self, filename):
        texts: list[str] = list()

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
                try:
                    doc = book.read(path).decode('utf-8')
                except KeyError:
                    try:
                        doc = book.read('OEBPS/' + path).decode('utf-8')
                    except KeyError:
                        print("Warning: couldn't find '" + path + "' in the archive.")
                        continue
                doc_tree = ET.fromstring(doc)
                texts.append(ET.tostring(
                    doc_tree, encoding='unicode', method='text'))

        return ''.join(texts)


if __name__ == '__main__':
    e = EpubTextExtractor(
        r'E:\Users\imbiansl\Downloads\picture us in the light_loy gilbert, kelly.epub')
    with open('test-text.txt', 'w') as f:
        f.write(e.get_text())
