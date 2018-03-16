# project euler no. 1
#   add all natural numbers below 1000 that are multiples of 3 or 5
#     answer = 233168

print sum(range(3, 1000, 3)) + sum(range(5, 1000, 5)) - sum(range(15,1000,15))
