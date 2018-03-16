# project euler no. 6
#   find the difference between the sum of squares and the square of sums for 1 to 100
#     answer = 25164150

def Square(x):
  return x**2

print ((sum(range(1,101)))**2)-(sum(map(Square,range(1,101))))
