import sys
import string

if len(sys.argv) is not 3:
    print("ERROR")
    exit(1)
line = sys.argv[1]
try:
    n = int(sys.argv[2])
except BaseException:
    print("ERROR, ARG 2 NOT A NUMBER")
    exit(1)
if len(line) <= n or n < 0:
    print("ERROR")
    exit(1)
for c in line:
    if c in string.punctuation:
        line = line.replace(c, "")
lst_wrd = line.split()
def_lst = []
for word in lst_wrd:
    if len(word) > n:
        def_lst.append(word)
print(def_lst)
