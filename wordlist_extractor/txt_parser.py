"""\
This file extracts words from a txt file.
"""
import re


def get_words_from_txt(pathname: str):
    """
    Get a list of words from a txt file.

    Args:
        pathname: The path to the txt file.

    Returns:
        A list of words.
    """
    words = set()
    with open(pathname, 'r') as f:
        for line in f:
            words.update({word.lower() for word in re.findall(r'\w+', line)})
    return words
