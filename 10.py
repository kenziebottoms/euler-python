# project euler no. 10
#   find the sum of all the prime numbers under 2 000 000
#     answer = 142913828922

#def is_prime(x):
#  for i in range (2,x/2+1):
#    if x % i == 0:
#      return False
#  return True

primes = []

def is_prime(x):
  for prime in primes:
    if x % prime == 0:
      return False
  primes.append(x)
  return True

for i in range(2,2000000):
  if is_prime(i):
    print i

print sum(primes)