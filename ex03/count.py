#!~/Miniconda3/bin/python3.7
import string


def text_analyzer(*arg):
    '''This Functions analyze the text'''
    up_letters = 0
    lower_letters = 0
    pct_marks = 0
    spcs = 0
    txt = ""
    if len(arg) > 1:
        print("ERROR")
        return
    elif len(arg) == 0:
        txt = input("What is the text to analyse?\n")
    else:
        txt = arg[0]
    print(isinstance(txt, str))
    if isinstance(txt, str) is False:
        print("ERROR")
        return

    for ch in txt:
        if ch in string.ascii_uppercase:
            up_letters += 1
        elif ch in string.ascii_lowercase:
            lower_letters += 1
        elif ch in string.punctuation:
            pct_marks += 1
        elif ch in string.whitespace:
            spcs += 1
    print("the text contains ", len(txt), "characters\n")
    print(up_letters, "upper letters\n")
    print(lower_letters, "lower letters\n")
    print(pct_marks, "punctuation marks\n")
    print(spcs, "spaces")
