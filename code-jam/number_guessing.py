import random
import sys
def read_two_inputs():
  res = raw_input().split(" ")
  a = int(res[0])
  b = int(res[1])
  return a,b

def guess(a,b):
  if a == b:
    return a
  return random.randint(a,b)

def start_program(t):
  for _ in xrange(0 , t ):
    a,b = read_two_inputs()
    if a == 0:
      a = 1
    n = int(raw_input())
    for _ in xrange(0, n ):
      guessed_num = guess(a,b)
      print guessed_num
      sys.stdout.flush()
      word = raw_input()
      if word == 'TOO_BIG':
        b = guessed_num - 1
      elif word == 'TOO_SMALL':
        a = guessed_num + 1
      elif word == 'CORRECT':
        break
    
# program starts
t = int(raw_input())
if  0 <= t and t <= 20:
    start_program(t)
else:
   print >>sys.stderr
