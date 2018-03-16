# project euler no. 4
#   find the largest palindromic product of two 3-digit numbers
#     answer = 906609

def products():
  products = []
  for i in range (100,1000):
    for j in range (100,1000):
      products.append(i*j)
  return products
  
def palendromic(x):
  return str(x) == str(x)[::-1]

print str(max(filter(palendromic,products())))
