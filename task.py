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
	
	print(output)
	

shiftEncrypt("Hello World")