# project euler no. 17
#  find how many letters would be used if all the numbers from 1 to 1000 were written out
#    answer = 21124

ones = {0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen'}
tens = {0:'',1:'ten',2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'}
hundreds = {}
for item in ones:
  hundreds[item] = ones[item]+'hundred'
hundreds[0] = ''

def keep_on(num,one_zeroes):
  for i in range(1,11):
    if (num - i*one_zeroes) < one_zeroes and (num - i*one_zeroes) >= 0:
      return i
  return 0

def value(num):
  value = hundreds[keep_on(num,100)]
  if num % 100 != 0 and num > 100:
    value += 'and'
  num -= 100*(keep_on(num,100))
  if num % 100 != 0:
    if num >= 20:
      value += tens[keep_on(num,10)]
      num -= 10*(keep_on(num,10))
      if num % 10 != 0:
        value += ones[keep_on(num,1)]
    elif num < 20:
      value += ones[num]
  return value

values = (map(value,range(1,1000)))
def sum_lengths(list):
  new_list = []
  for item in list:
    new_list.append(len(item))
  return new_list
print sum(sum_lengths(values))+11
