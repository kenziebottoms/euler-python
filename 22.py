# project euler no. 22
#   find the total of all the name-scores in names.txt
#     answer = 871198282

import urllib

names = urllib.urlopen('http://projecteuler.net/project/names.txt','r').read()
names = names.strip('\"').split('\",\"')
names.sort()

def find_namescore(name):
  alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
  namescore = 0
  for letter in name:
    namescore += alphabet[letter]
  return namescore

def find_weighted_namescores(names):
  weighted_namescores = []
  index = 1
  for name in names:
    weighted_namescores.append(find_namescore(name)*index)
    index += 1
  return weighted_namescores

print sum(find_weighted_namescores(names))
