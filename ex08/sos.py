import sys
import string

morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'}

if len(sys.argv) < 2:
    exit(0)
word = []
for line in sys.argv:
    word.append(line)
word.remove(word[0])
for line in word:
    if '/' in line:
        print("ERROR")
        exit(1)
i = 0
for line in word:
    if i > 0:
        print("/ ", end='')
    i += 1
    line = line.upper()
    for c in line:
        if c in string.whitespace:
            print(" / ", end='')
        else:
            print(morse_code[c], end='')
            print(" ", end='')
print()
