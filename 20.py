# project euler no. 20
#   find the sum of digits in the number 100!
#     answer = 648

import math

sum_of_digits = 0
for digit in str(math.factorial(100)):
  sum_of_digits += int(digit)
print sum_of_digits
