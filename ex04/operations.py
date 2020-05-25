#!~/Miniconda3/bin/python3.7
import sys

def calcul(a, b):
	add = a + b
	sub = a - b
	prd = a * b
	if b == 0:
		qut = "ERROR (div by zero)"
		rem = "ERROR (modulo by zero)"
	else:
		qut = a / b
		rem = a % b
	return add, sub, prd, qut, rem


inp_err = "InputError: too many arguments\n\n"
num_error = "InputError: only numbers\n\n"
usg_err = "Usage: python operations.py <number1> <number2>\nExample:\n	python operations.py 10 3"

if len(sys.argv) < 3:
	print(usg_err)
	exit(1)
elif len(sys.argv) > 3:
	print(inp_err + usg_err)
	exit(1)
try:
	a = int(sys.argv[1])
except BaseException:
	print(num_error + usg_err)
	exit(1)
try:
	b = int(sys.argv[2])
except BaseException:
	print(num_error + usg_err)
	exit(1)

add,dif,prd,qut,rem = calcul(a, b)

print("Sum:		", add)
print("Difference:	", dif)
print("Product:	", prd)
print("Quotient:	", qut)
print("Remainder	", rem)
