#!~/Miniconda3/bin/python3.7
import sys
import string

nbr_arg = len(sys.argv)

if nbr_arg <= 1:
    exit(1)

nbr_arg -= 1
line = sys.argv[nbr_arg]
line = line[::-1]
nbr_arg -= 1

while nbr_arg > 0:
    tmp = sys.argv[nbr_arg]
    tmp = tmp[::-1]
    line = line + " " + tmp
    nbr_arg -= 1

print(line.swapcase())
