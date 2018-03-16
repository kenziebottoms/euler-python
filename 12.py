# project euler no. 12
#   find the first triangle number to have over 500 divisors
#     answer = 76576500

import math

triangles = [0]

def triangle_number(term):
  term = (term*(term+1))/2
  return term

def find_number_of_divisors(x):
  divisors = [1,x]
  for i in range(2,x/2+1):
    if x % i == 0:
      divisors.append(i)
  return len(divisors)

x = 10000
while find_number_of_divisors(triangle_number(x)) <= 500:
  x += 1
  print triangle_number(x)