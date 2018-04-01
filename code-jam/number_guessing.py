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
  return random.randrange(a,b)

def start_program(t,a,b,n):
  for _ in xrange(1, t + 1):
    tmp_a = a
    tmp_b = b
    for _ in xrange(1, n + 1):
      guessed_num = guess(a,b)
      print guessed_num
      sys.stdout.flush()
      word = raw_input()
      if word == 'TOO_BIG':
        if (guessed_num -1) < a:
          b = b
        else:
          b = guessed_num - 1
      elif word == 'TOO_SMALL':
        if (guessed_num + 1) > b:
          a = a
        else:
          a = guessed_num + 1
      elif word == 'CORRECT':
        a = tmp_a
        b = tmp_b
        break
    
# program starts
t = int(raw_input())
if  0 <= t and t <= 20:
  a,b = read_two_inputs()
  if a >= 0 and b <= 30:
    if a == 0:
      a = 1
    n = int(raw_input())
    start_program(t, a, b, n)
  else:
     print >>sys.stderr, "A value and B value are incorrect"
else:
   print >>sys.stderr, "Number T is higher"
