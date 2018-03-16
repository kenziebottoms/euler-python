def product(list):
  product = 1
  for item in list:
    product = product * int(item)
  return product

def even(x):
  return x % 2 == 0

def palendromic(x):
  return str(x) == str(x)[::-1]

def square(x):
  return x**2

def is_prime(x):
  for i in range (2,x/2+1):
    if x % i == 0:
      return False
  return True

def false_factorial(x):
  factorial = 0
  for i in range(1,x+1):
    factorial += i
  return factorial
