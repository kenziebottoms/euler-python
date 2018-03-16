# project euler no. 3
#   find the largest prime factor of 600851475143
#     answer = 6857

magic_number = 600851475143

def divide(magic_number):
  for i in range(3,10000,2):
    if magic_number % i == 0:
      print i
      magic_number = magic_number/i
  return magic_number

divide(magic_number)
