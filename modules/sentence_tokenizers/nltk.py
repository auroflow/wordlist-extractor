from nltk.tokenize import sent_tokenize


class NltkSentTokenizer:
    def get_sentences(self, text: str):
        sentences: list[str] = list()
        
        for line in text.split("\n"):
            line = line.strip()
            if line:
                new_sentences = sent_tokenize(line)
                if new_sentences:
                    sentences.extend(new_sentences)

        return sentences


if __name__ == '__main__':
    with open('test-text.txt') as f:
        text = f.read()

    t = NltkSentTokenizer(text)
    sentences = t.get_sentences()

    with open('test-sentence.txt', 'w') as f:
        for sentence in sentences:
            f.write(sentence + '\n')
