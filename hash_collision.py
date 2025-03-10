'''
Produce a hash collision in a new hash function we'll call MD1.25.

MD1.25 is just MD5 truncated to the first 4 bytes (the first 8 digits in hex). Thus, MD1.25 only has a digest size of 32 bits. You should be able to produce a collision in no more than a couple seconds.

To prove that you generated the hash collision yourself, you must prefix your preimages with the string "nakamoto". Your code should return a tuple of the two colliding preimages as strings. 
'''

from hashlib import md5
import time

start_time = time.time()

def md125(s: str) -> str: # use this hash function to generate a collision
  return md5(s.encode()).hexdigest()[:8]

def generate_md125_collisions() -> (str, str):
  d = {}

  for i in range(2**16 + 1):
    n = md125("nakamoto"+str(i))
    if n in d:
      t = ("nakamoto"+str(d[n]), "nakamoto" + str(i))
      print(t)
      break
    d[n] = i
  #print(l)

generate_md125_collisions()
print("--- %s seconds ---" % (time.time() - start_time))