import random
import sympy

encrypted_msg = ''
plain_msg = ''

def rsa(symbol):
	global encryption, decryption
	p = sympy.randprime(1,90)
	q = sympy.randprime(1,90)

	n = p*q

	t = (p-1)*(q-1)

	e = sympy.randprime(1, t-1)

	while t%e == 0:
		e = sympy.randprime(1, t-1)

	max = 90
	d = random.randrange(1,max)

	while (d*e)%t != 1:
		max+=10
		d = random.randrange(1,max)

	encryption = (symbol**e)%n
	decryption = (encryption**d)%n

def enc_char(char):
	global e
	rsa(ord(char))
	return chr(encryption)

def dec_char(char):
	global e
	rsa(ord(char))
	return chr(decryption)

message = input("Message: ")

for i in message:
	encrypted_msg+=str(enc_char(i))

for i in message:
	plain_msg+=str(dec_char(i))

print("Encryption: "+encrypted_msg)
print("Decryption: "+plain_msg)
