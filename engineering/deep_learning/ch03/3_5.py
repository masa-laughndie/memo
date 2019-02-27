import numpy as np
import matplotlib.pylab as plt

def softmax(a):
  c = np.max(a)
  e_a = np.exp(a - c)
  sum_e_a = np.sum(e_a)
  y = e_a / sum_e_a
  return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
s = np.sum(y)
print(s)