# project euler no. 25
#   find the first Fibonacci term to contain 1000 digits
#     answer = 4782

terms = {1:1, 2:1}  # Terms = {term in sequence:number}

def count_digits(number):
  count = 0
  for digit in str(number):
    count += 1
  return count

i = 3
while True:
  terms[i] = terms[i-1] + terms[i-2]
  print terms[i]
  if count_digits(terms[i]) >= 1000:
    print i
    break
  i += 1
