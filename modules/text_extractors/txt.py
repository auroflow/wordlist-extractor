from . import TextExtractor


class TxtTextExtractor(TextExtractor):
    """\
    This class extracts texts from txt files.
    """

    def get_text(self, filename):
        with open(filename, encoding="utf-8") as f:
            text = f.read()
        return text
