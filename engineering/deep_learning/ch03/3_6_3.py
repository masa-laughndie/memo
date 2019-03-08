import numpy as np
import matplotlib.pylab as plt
import sys, os
sys.path.append(os.pardir)
from function import active_functions as af
# from function.utils import p
from dataset.mnist import load_mnist
from PIL import Image
import pickle
pf = __import__("3_6_2")



x, t = pf.get_data()
network = pf.init_network()

batch_size = 10000 # バッチの数
accurracy_cnt = 0

for i in range(0, len(x), batch_size):
  x_batch = x[i:i+batch_size]
  y_batch = pf.predict(network, x_batch)
  p = np.argmax(y_batch, axis=1)
  accurracy_cnt += np.sum(p == t[i:i+batch_size])

print(x)
print("Accurracy:" + str(float(accurracy_cnt) / len(x)))

x = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.3, 0.3], [0.8, 0.1, 0.1]])
y = np.argmax(x, axis=0)
print(y)