# project euler no. 48
#   find the sum of the sequence: 1^1 + 2^2 + 3^3 + ... + 1000^1000
#     answer = 9110846700

def exp(x):
  return x**x

print sum(map(exp,range(1,1001)))
