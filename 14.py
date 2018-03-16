# project euler no. 14
#   find the staring number under 1 000 000 that results in the longest Collatz sequence
#     answer = 837799

Terms = {1: 1}  # Terms = {natural number: terms to 1}

def terms_to_one(x):
  x_prime = x
  i = 0
  while not x_prime in Terms:
    if x_prime % 2 == 0:
      x_prime = x_prime/2
      i += 1
    else:
      x_prime = 3*x_prime + 1
      i += 1
  i += Terms[x_prime]
  Terms[x] = i
  return i

max = 0
for i in range(1000000,1,-1):
  if terms_to_one(i) > max:
    max = terms_to_one(i)
    print i, max