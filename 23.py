# project euler no. 23
#   find the sum of all positive integers that cannot be written as the sum of two abundant numbers

from sets import Set

def is_abundant(x):
  return sum(get_divisors(x)) > x
    
def is_sum_of_abundants(n,abundants):
  for x in [x for x in abundants if x < n]:
    for y in [y for y in abundants if y < n]:
      if x+y == n:
        print x,"+",y,"=",n
        return True
  return False

def get_divisors(x):
  divisors = [1]
  for i in range(2,x/2+1):
    if x % i == 0:
      divisors.append(i)
  return divisors

abundants = Set(filter(lambda x:is_abundant(x), Set(range(12,28124))))
sums = Set(filter(lambda x:is_sum_of_abundants(x, abundants), Set(range(1,28124))))
nonsums = Set(range(1,28124)) - sums
print sum(nonsums)