# project euler no. 2
#   find the sum of the even terms in the Fibonacci sequence whose values don't exceed 4 000 000
#     answer = 4613732

fib = [1,1]
for i in range(0,31):
  fib.append(fib[-2] + fib[-1])

def evens(x):
  return x % 2 == 0

print sum(filter(evens, fib))
