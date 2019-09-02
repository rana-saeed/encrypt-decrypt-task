import sys
from string import ascii_lowercase as ALPHABETLOWER
from string import ascii_uppercase as ALPHABETUPPER

def shiftEncrypt(s):
	offset = 3
	output = ""

	for c in s:
		if c in ALPHABETLOWER:
			output = ''.join((output, chr(ord(c) + offset)))
		elif c in ALPHABETUPPER:
			output = ''.join((output, chr(ord(c) + offset)))
		else:
			output = ''.join((output, c))
	
	return output
	

def matrixEncrypt(s):

	with open('matrix.txt') as m:
		matrix = m.read()
	
	matrix = [list(map(float, item.split())) for item in matrix.split('\n')[:-1]]
	binChars = []

	for c in s:
		binCharStr = (bin(int.from_bytes(c.encode(), 'big'))[2:]).zfill(16)
		binChar = list(map(int, binCharStr))
		binChars.append(binChar)

	matrixResult = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrix)] for X_row in binChars]
	return matrixResult

print(shiftEncrypt("Hello World"))
print(matrixEncrypt("Hello World"))