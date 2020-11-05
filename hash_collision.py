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