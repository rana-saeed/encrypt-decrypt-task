import sys
import requests
from string import ascii_lowercase as ALPHABETLOWER
from string import ascii_uppercase as ALPHABETUPPER

#Encryting a string by shifting each character 3 positions in the alphbet
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
	
#Encrytping a string by:
#	1.Converting each ascii char to its binary format (length 16)
#	2.Creating a nx16 matrix representing the binary format of the string (where n is the length of the string)
#	3.Multiplying the nx16 matrix with the encryption matrix provided
#	4.Converting matrix into an encoded string where each comma seperated line represents a character and space seperated characters represent a word
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
	
	#Convert matrix result to string
	matrixStr= ""
	for row in matrixResult:
		str1 = ""
		for element in row:
			if(len(str1) == 0):
				str1 = ''.join((str1,str(element)))
			else:
				str1 = ','.join((str1,str(element)))

		if(len(matrixStr) == 0):
			matrixStr = ''.join((matrixStr,str1))
		else:
			matrixStr = ' '.join((matrixStr,str1))

	return matrixStr

#Decrypting a string by shifting each character -3 positions in the alphabet
def shiftDecrypt(s):
	offset = 3
	output = ""

	for c in s:
		if c in ALPHABETLOWER:
			output = ''.join((output, chr(ord(c) - offset)))
		elif c in ALPHABETUPPER:
			output = ''.join((output, chr(ord(c) - offset)))
		else:
			output = ''.join((output, c))
	
	return output

#Decrypting a string by:
#	1.Converting the string into a nx16 matrix where n is the length of the string
#	1.Multiplying the nx16 matrix with the inverse decryption matrix provided
#	2.Getting the binary format of each matrix row result
#	3.Conveting the binary result to ascii format to represent each of the characters in the string
def matrixDecrypt(s):
	s = [[float(x) for x in ss.split(',')] for ss in s.split(' ')]
	with open('inverse.txt') as m:
		matrixInverse = m.read()

	matrixInverse = [list(map(float, item.split())) for item in matrixInverse.split('\n')[:-1]]
	matrixResult = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrixInverse)] for X_row in s]

	resultStr = ""
	for i in matrixResult:
		binStr = "0b"
		for j in i:
			binStr = ''.join((binStr, str(round(j))))

		n = int(binStr, 2)
		n = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
		resultStr = ''.join((resultStr, n))

	return resultStr

#Encrypting a string through external encoding API
def postEncode(s):
	url = 'http://backendtask.robustastudio.com/encode'
	payload = "{\n\t\"string\" : " + "\"" + s + "\"\n}"
	headers = {
		'Content-Type': 'application/json'
	}
	response = requests.request('POST', url, headers = headers, data = payload, allow_redirects = False)
	return response.json().get('string')

#Decrypting a string through external decoding API
def postDecode(s):
	url = 'http://backendtask.robustastudio.com/decode'
	payload = "{\n\t\"string\" : " + "\"" + s + "\"\n}"
	headers = {
		'Content-Type': 'application/json'
	}
	response = requests.request('POST', url, headers = headers, data = payload, allow_redirects = False)
	return response.json().get('string')

# print(shiftEncrypt("Hello World"))
# print(shiftDecrypt("Khoor Zruog"))

# print(matrixEncrypt("Hi"))
# print(matrixDecrypt("9.0,6.0,12.0,7.0,13.0,8.0,13.0,9.0,4.0,8.0,8.0,6.0,6.0,11.0,13.0,5.0 20.0,21.0,13.0,18.0,17.0,18.0,15.0,9.0,6.0,22.0,17.0,14.0,17.0,29.0,24.0,5.0"))
# print(matrixEncrypt("Hey"))
# print(matrixDecrypt("9.0,6.0,12.0,7.0,13.0,8.0,13.0,9.0,4.0,8.0,8.0,6.0,6.0,11.0,13.0,5.0 18.0,19.0,5.0,22.0,8.0,13.0,14.0,10.0,5.0,22.0,20.0,20.0,18.0,27.0,20.0,12.0 29.0,28.0,20.0,21.0,18.0,23.0,16.0,9.0,15.0,27.0,21.0,23.0,20.0,35.0,30.0,5.0"))
# print(matrixEncrypt("Hello World"))
# print(matrixDecrypt("9.0,6.0,12.0,7.0,13.0,8.0,13.0,9.0,4.0,8.0,8.0,6.0,6.0,11.0,13.0,5.0 18.0,19.0,5.0,22.0,8.0,13.0,14.0,10.0,5.0,22.0,20.0,20.0,18.0,27.0,20.0,12.0 19.0,14.0,13.0,21.0,15.0,17.0,21.0,18.0,8.0,22.0,17.0,15.0,14.0,27.0,18.0,14.0 19.0,14.0,13.0,21.0,15.0,17.0,21.0,18.0,8.0,22.0,17.0,15.0,14.0,27.0,18.0,14.0 28.0,25.0,18.0,27.0,26.0,24.0,28.0,20.0,10.0,36.0,25.0,21.0,29.0,43.0,28.0,16.0 6.0,6.0,0.0,7.0,2.0,7.0,1.0,0.0,2.0,6.0,4.0,2.0,2.0,9.0,4.0,0.0 25.0,22.0,16.0,20.0,16.0,15.0,20.0,12.0,14.0,27.0,23.0,27.0,25.0,31.0,25.0,14.0 28.0,25.0,18.0,27.0,26.0,24.0,28.0,20.0,10.0,36.0,25.0,21.0,29.0,43.0,28.0,16.0 22.0,17.0,14.0,16.0,16.0,17.0,13.0,3.0,14.0,17.0,17.0,16.0,12.0,24.0,21.0,5.0 19.0,14.0,13.0,21.0,15.0,17.0,21.0,18.0,8.0,22.0,17.0,15.0,14.0,27.0,18.0,14.0 13.0,10.0,4.0,18.0,6.0,10.0,13.0,10.0,5.0,14.0,15.0,14.0,9.0,18.0,13.0,12.0"))

print(postEncode("Hello World"))
print(postDecode("dlrow olleH"))