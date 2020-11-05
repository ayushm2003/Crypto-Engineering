#######################################
#              PART 1                 #
#######################################

from hashlib import sha256

def h(s): return sha256(s.encode()).hexdigest() # hashing helper function


def base(sentence: str) -> list:
	'''Hash the base layer, padding excluded'''
	words = sentence.split()  # creates list of words in the sentence

	hashed = []

	# hashes the elements and adds it to the list
	for word in words:
		hashed.append(h(word))
	
	return hashed


def tree(root: list) -> str:
	'''merkliezes the hashed base list with padding, down to the root'''

	while len(root) != 1:  # when length == 1, it is the root
		branch = []

		# i increments over 2 values, therefore hashing the two adjacent elements
		for i in range(0, len(root), 2):
			branch.append(h(root[i] + root[i+1]))  # hashes and adds it to the list

		root = branch

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

print(merklieze("Unbelievable..."))