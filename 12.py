# project euler no. 12
#   find the first triangle number to have over 500 divisors
#     answer = 76576500

import math

triangles = [0]

def triangle_number(term):
  term = (term*(term+1))/2
  return term

def divisors(x):
  divisors = [1,x]
  i = 2;
  while x >= i and i < math.sqrt(x):
    if x % i == 0:
      divisors.append(i)
      divisors.append(x/i)
    i += 1
  return divisors

x = 12350
while len(divisors(triangle_number(x))) <= 500:
  x += 1
  print triangle_number(x)