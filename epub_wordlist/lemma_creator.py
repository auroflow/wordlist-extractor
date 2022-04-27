"""\
This file parses the lemma file and creates a dict object storing mappings from
words to their lemmas.

The format for each line of the lemma file:

  lemma\t word1 word2 ...

Example:

  a an

A line starting with ';' is a comment.
"""


_cached_mapping: dict[str, str] | None = None


def get_mapping(lemma_filename: str) -> dict[str, str]:
    """
    Get a dict object storing mappings from words to their lemmas.

    Args:
        lemma_filename: The file containing the lemma mappings.

    Returns:
        A dict object storing mappings from words to their lemmas.
    """
    global _cached_mapping
    if _cached_mapping is not None:
        return _cached_mapping

    mapping: dict[str, str] = dict()
    lemmas: set[str] = set()

    with open(lemma_filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            words = line.split()
            lemmas.add(words[0])
            for word in words:
                if word in lemmas:
                    mapping[word] = word
                else:
                    mapping[word] = words[0]
    _cached_mapping = mapping
    return mapping
