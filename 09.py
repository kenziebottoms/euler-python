# project euler no. 9
#   find the only Pythagorean triplet for which a + b + c = 1000
#     answer = 31875000

import math

def pyth():
  for a in range(1,1001):
    for b in range(1001-a):
      c = math.sqrt(a*a + b*b)
      if (a + b + c) == 1000:
        return a*b*c

print pyth()
