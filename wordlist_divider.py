import re
import sys
from keyboard import read_event
from random import shuffle
from argparse import ArgumentParser

filename = 'wordlist.txt'
prompt = "[F] I don't know this word  [J] I know this word  [Z] Undo last word  [Esc] Quit"


def clear():
    print("\033[H\033[J")


class StatusBar:
    def __init__(self, total, width=100):
        self.total = total
        self.current = 0
        self.width = width

    def update(self, i):
        self.current = i

    def __str__(self):
        percentage = self.current / self.total
        return '|' + '#' * round(percentage * self.width) + ' ' * \
            round((1 - percentage) * self.width) + \
            f'| {self.current}/{self.total} ({percentage*100:.1f}%)'


parser = ArgumentParser()
parser.add_argument('-f', '--filename',
                    help='The path to the word list.', default=filename)
args = parser.parse_args()
if args.filename:
    filename = args.filename

with open(filename, 'r') as f:
    words = re.findall('\w+', f.read())
    shuffle(words)
    bar = StatusBar(len(words))
    known = [None for _ in words]
    i = 0
    while i < len(words):
        clear()
        bar.update(i)
        print(bar)
        print((('You know ' if known[i - 1] else "You don't know ") +
              repr(words[i - 1]) + '.') if i > 0 else 'Welcome!')
        print('┌─' + '─' * len(words[i]) + '─┐')
        print('│ ' + words[i] + ' │')
        print('└─' + '─' * len(words[i]) + '─┘')
        print(prompt)
        while True:
            event = read_event()
            if event.event_type == 'up':
                continue
            if event.name == 'f':
                known[i] = False
                i += 1
            elif event.name == 'j':
                known[i] = True
                i += 1
            elif i > 0 and event.name == 'z':
                i -= 1
                known[i] = None
            elif event.name == 'esc':
                sys.exit(0)
            else:
                print(event.name)
                continue
            break

if filename.endswith('.txt'):
    filename = filename[:-4]

with open(f'{filename}.known.txt', 'w') as known_file:
    with open(f'{filename}.unknown.txt', 'w') as unknown_file:
        for i, word in enumerate(words):
            if known[i] == True:
                known_file.write(word + '\n')
            elif known[i] == False:
                unknown_file.write(word + '\n')

# Eat the input
clear()
input('Done. Press Enter to exit.\n')
