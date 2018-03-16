# project euler no. 21
#   find the sum of all amicable numbers under 10000
#     answer = 31626

def find_divisors(x):
  divisors = []
  for i in range(1,(x/2)+1):
    if x % i == 0:
      divisors.append(i)
  return divisors

def is_amicable(x):
  for divisor in find_divisors(x):
    if sum(find_divisors(sum(find_divisors(x)))) == x and sum(find_divisors(x)) != x:
      return True
  return False

def find_amicables(upper_bound):
  amicables = []
  for i in range(2,upper_bound):
    if is_amicable(i):
      amicables.append(i)
      print i
  return sum(amicables)

print find_amicables(10000)
#print is_amicable(2)
