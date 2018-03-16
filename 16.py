# project euler no. 16
#   find the sum of the digits of 2^1000
#     answer = 1366

magic_number = str(2**1000)

def count(num):
  count = 0
  for digit in num:
    count += int(digit)
  return count

print count(magic_number)
