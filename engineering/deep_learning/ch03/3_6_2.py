import numpy as np
import matplotlib.pylab as plt
import sys, os
sys.path.append(os.pardir)
from function import active_functions as af
from dataset.mnist import load_mnist
from PIL import Image

def get_data():
  (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
  return x_test, t_test

def init_network():
  with open("sample_weight.pkl", "rb") as f:
    network = pickle,load(f)

  return network

def predict(network, x):
  W1, W2, W3 = network['W1'], network['W2'], network['W3']
  b1, b2, b3 = network['b1'], network['b2'], network['b3']

  a1 = np.dot(x, W1) + b1
  z1 = af.sigmoid(a1)
  print(z1)
  a2 = np.dot(z1, W2) + b2
  z2 = af.sigmoid(a2)
  a3 = np.dot(z2, W3) + b3
  y = af.indentity_function(a3)

  return y

x, t = get_data()
network = init_network()

accurracy_cnt = 0
for i in range(len(x)):
  y = predict(network, x[i])
  p = np.argmax(y)

  if p == t[i]:
    accurracy_cnt += 1

print("Accurracy:" + str(float(accurracy_cnt)/ len(x)))