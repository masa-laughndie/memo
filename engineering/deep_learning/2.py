import numpy as np

def p(s):
  print(s)


x = np.array([0, 1])
p(x)
w = np.array([0.5, 0.5])
p(w)
b = - 0.7
p(w * x)
p(np.sum(w * x))
p(np.sum(w * x) + b)


def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = - 0.7
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = 0.7
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = - 0.2
  tmp = np.sum(w * x) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def XOR(x1, x2):
  s1 = NAND(x1, x2)
  s2 = OR(x1, x2)
  return AND(s1, s2)

p(XOR(0,0))
p(XOR(1,0))
p(XOR(0,1))
p(XOR(1,1))