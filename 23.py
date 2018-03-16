# project euler no. 23
#   find the sum of all positive integers that cannot be written as the sum of two abundant numbers


#ID FUNCTIONS

def is_abundant(x):
  if sum(get_divisors(x)) > x:
    return True
  return False

def is_sum_of_abundants(x,abundants):
  for item in abundants:
    for item2 in abundants:
      if item+item2 == x:
        return True
  return False


#GET FUNCTIONS

def get_divisors(x):
  divisors = [1]
  for i in range(2,x/2+1):
    if x % i == 0:
      divisors.append(i)
  return divisors

#print get_divisors(12)

def get_abundants():
  abundants = []
  for i in range(12,28124):
    if is_abundant(i):
      print i
      abundants.append(i)
  return abundants

get_abundants()

def get_sums(abundants):
  sums = []
  for i in range(0,28124):
    if is_sum_of_abundants(i,abundants):
      sums.append(i)
  return sums

def get_nonsums(sums):
  nonsums = []
  for i in range(0,28124):
    if not i in sums:
      nonsums.append(i)
  return nonsums


#EXECUTION

#abundants = get_abundants()
#print abundants[0:100]
#print is_sum_of_abundants(24,abundants)
#print is_sum_of_abundants(27,abundants)
#print is_sum_of_abundants(30,abundants)
#sums = get_sums(abundants)
#nonsums = get_nonsums(sums)
#print sum(nonsums)
