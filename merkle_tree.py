#######################################
#              PART 1                 #
#######################################

from hashlib import sha256
import time

start_time = time.time()

def h(s): return sha256(s.encode()).hexdigest() # hashing helper function


def base(sentence: str) -> list:
	'''Hash the base layer, padding excluded'''
	words = sentence.split()  # creates list of words in the sentence

	hashed = []

	# hashes the elements and adds it to the list
	for word in words:
		hashed.append(h(word))
	
	#print(hashed)
	return hashed


def tree(root: list) -> str:
	'''merkliezes the hashed base list with padding, down to the root'''

	while len(root) != 1:  # when length == 1, it is the root
		branch = []

		# i increments over 2 values, therefore hashing the two adjacent elements
		for i in range(0, len(root), 2):
			branch.append(h(root[i] + root[i+1]))  # hashes and adds it to the list

		root = branch
		#print(root)

	# returns the root as a string
	return root[0]

def merklieze(sentence: str) -> str:
	'''Combines all the functions and adds the padding'''
	hash = base(sentence)  # hash of base layer

	length = len(hash)

	if length == 1:  # 1 was a weird corner case, thus explicit add
		return hash[0]
	else:  # adds padding ('\x00') if not power of 2
		p = 1
		for i in range(length):
			if p < length:
				p *= 2
			else:
				n = (2**i) - length

				if n == 0: break  # if power of 2
				else:  # if not power of 2
					for j in range(n):
						hash.append(chr(0))
				
				break
	
	# passes the list to function tree() and returns the value recieved
	return tree(hash)

'''
with open('merkle_instructions.txt', 'r') as file:
	st = file.read()
'''
print(merklieze('Lavana Loves Browny!!!!'))
'''
print(merklieze('a b c d'))
string1 = """
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d 
2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc618ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4
"""
#print(merklieze(string1))
#print(merklieze('62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154dad3a0f1c792ccf7f1708d5422696263e35755a86917ea76ef9242bd4a8cf4891a'))
print(tree(['96e024ba2074fe77e8e965ba43a704be', 'c0a594722e66ed5e4dec538fdc1fc1ba']))
'''
print("--- %s seconds ---" % (time.time() - start_time))