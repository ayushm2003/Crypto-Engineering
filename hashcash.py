from hashlib import sha256

def h(s): return sha256(s.encode()).hexdigest() # hashing helper function

def binary_leading_0s(hex_str: str):
	binary_representation = bin(int(hex_str, 16))[2:].zfill(256)
	return len(binary_representation) - len(binary_representation.lstrip('0'))

def is_valid(token: str, date: str, email: str, difficulty: int) -> bool:
	# Splits token based on :
	# Ideal Token format - VERSION:DATE:EMAIL:NONCE
	
	elements = token.split(":")
	
	if len(date) > 6:
		return False
	elif elements[1] != date or elements[2] != email:
		return False
	elif len(elements[3]) > 16:
		return False

	hash = h(token)
	n = binary_leading_0s(hash)

	return False if n < difficulty else True

flag = is_valid('1:satoshin@gmx.com:081031:248d07e28506851d', '081031', 'satoshin@gmx.com', 16)
print(flag)
#print(type(flag))

def mint(date: str, email: str, difficulty: int) -> str:
	version = "1"

	i = 0
	while True:
		a = hex(i).lstrip("0x")
		i += 1
		if len(a) <= 16:
			token = version + ":" + date + ":" + email + ":" + a
			hash = h(token)
			n = binary_leading_0s(hash)

			if n >= difficulty:
				print(token)
				return token
		else:
			return "Not found"

k = is_valid(mint('081031', 'satoshin@gmx.com', 20), '081031', 'satoshin@gmx.com', 9)
print(k)