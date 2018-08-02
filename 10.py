# project euler no. 10
#   find the sum of all the prime numbers under 2 000 000
#     answer = 142913828922

import math
primes = [2]

def is_prime(x):
  for prime in primes:
    if x % prime == 0:
      return False
    if math.sqrt(x) < prime:
      break
  primes.append(x)
  return True

for i in range(3,2000000,2):
  if is_prime(i) and (str(i)[-3:] == "317"):
    print i

print sum(primes)