from enum import Enum
from hashlib import sha256, sha1
import time

start_time = time.time()

def h(s): return sha256(s.encode()).hexdigest() # hashing helper function

class Side(Enum):
	LEFT = 0
	RIGHT = 1

def validate_proof(root: str, data: str, proof: [(str, Side)]) -> bool:
	data_hash = h(data)  # hash of block to find

	n = data_hash

	for pr in proof:  # iterate over every element in the list
		sibling = pr[0]  # the sibling hash
		s = pr[1]  # the side they are on
		left = Side.LEFT  # saving the LEFT one for comparison

		# hashing is done as LEFT element + RIGHT element
		if s is left:
			x = h(sibling + n)
		else:
			x = h(n + sibling)
		
		n = x  # changing the last known block every time
	
	if n == root:  # if the final block == root
		return True
	else:
		return False
		

a = validate_proof("ac5544f3322e06322c6740a7c428c5cf9f2f33b88a023a3aad6d7199c31cbe29", "love", [('a83dd0ccbffe39d071cc317ddf6e97f5c6b1c87af91919271f9fa140b0508c6c', Side.LEFT), ('355774732410d0b5b8f8be83b7c53aa69ad645b72d2feafbbac27e22ef791c29', Side.RIGHT)])
print(a)
print("--- %s seconds ---" % (time.time() - start_time))