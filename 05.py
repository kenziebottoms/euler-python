# project euler no. 5
#   find the smallest natural number evenly divisible by each number 1 to 20
#     answer = 232792560

#def divisible_by_all(lower_bound,upper_bound,start):
#  x = start
#  while True:
#    for i in range(lower_bound,upper_bound+1):
#      if x % i != 0:
#        break
#      elif i == upper_bound:
#        return x
#    x += 1

divisors = [20,19,18,17,16,15,14,13,12,11]

def divisible_by_all(x, divisors):
  for divisor in divisors:
    if x % divisor != 0:
      return False
  return True

x = 232000000
while True:
  print x
  if divisible_by_all(x, divisors):
    break
  x += 20