import numpy as np
import matplotlib.pylab as plt

def step_function(x):
  return np.array(x > 0, dtype = np.int)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def relu(x):
  return np.maximum(0, x)

def indentity_function(x):
  return x

def softmax(a):
  c = np.max(a)
  e_a = np.exp(a - c)
  sum_e_a = np.sum(e_a)
  y = e_a / sum_e_a
  return y
