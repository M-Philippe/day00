#!~/Miniconda3/bin/python3.7
import sys

arg_len = len(sys.argv)

if arg_len != 2:
    print("ERROR.")
    exit(1)

arg_len -= 1

try:
    nbr = int(sys.argv[arg_len])
except BaseException:
    print("ERROR.")
    exit(1)

if nbr == 0:
    print("I'm Zero.")
elif nbr % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
