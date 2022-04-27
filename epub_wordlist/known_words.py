"""\
This file reads from the files containing known words to generate a set of 
known lemmas.

Any words that appear after ';' in a line will be ignored.
"""
import os
import re


def get_known_lemmas(pathname: str, mapping: dict):
    """
    Get a set of known lemmas from the files containing known words.

    Args:
        pathname: The directory containing known word files.
        mapping: A dictionary mapping words to their respective lemmas.

    Returns:
        A set of known lemmas.
    """
    known_lemmas: set[str] = set()

    if not os.path.exists(pathname):
        return known_lemmas

    for filename in os.listdir(pathname):
        fullname = os.path.join(pathname, filename)
        if not os.path.isfile(fullname):
            continue
        with open(fullname, 'r') as f:
            for line in f:
                line = line.split(';')[0].strip()
                words: list[str] = re.findall(r'\w+', line)
                for word in words:
                    word = word.lower()
                    if word in mapping:
                        known_lemmas.add(mapping[word])
    return known_lemmas
