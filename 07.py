# project euler no. 7
#   find the 10001st prime number
#     answer = 104743

primes = []

def is_prime(x):
  for prime in primes:
    if x % prime == 0:
      return False
  primes.append(x)
  return True

i = 2

while len(primes) < 10001:
  if is_prime(i):
    print i
  i += 1