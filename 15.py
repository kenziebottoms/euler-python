# project euler no. 15
#   find the number of different routes from one corner to the other of a 20x20 grid
#     answer = 137846528820

def false_factorial(x):
  factorial = 0
  for i in range(1,x+1):
    factorial += i
  return factorial

def pyramid_number_terms(x):
  terms = []
  for i in range(1,x+1):
    terms.append(i)
  return terms

def find_routes(x):
  terms = pyramid_number_terms(x)
  terms.reverse()
  count = false_factorial(x)+1+x
  for i in range(3,x+1):
    terms_prime = []
    for i in range(len(terms)):
      terms_prime.append(sum(terms))
      terms.pop(0)
    terms = terms_prime[:]
    count += sum(terms)
  return count

print find_routes(20)
