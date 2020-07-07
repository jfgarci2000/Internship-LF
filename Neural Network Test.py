# Author: Juan Felipe Garcia
# This code is to test the Neural Network

import mnist_loader
import network
import compute_t
import numpy as np
import scipy.spatial.distance as sp

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

v = list(training_data)
# print( list(training_data))
#
x = v[0][0]
y = v[1][0]
(t, x1, y1, d1) = (compute_t.get_t(v[0][0], v[1][0], np.identity(784)))

print(sp.euclidean(v[0][0], v[1][0]))

net = network.Network([784, 30, 10])

net.SGD(training_data, 2, 10, 3.0, test_data=test_data)

#print(net.weights)

(t2, x2, y2, d2) = (compute_t.get_t(v[0][0], v[1][0], net.weights[0]))

from matplotlib import pyplot as plt
plt.gray()
# plt.imshow(np.reshape(x, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(x1, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(y, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(y1, (28,28)), interpolation='nearest')
# plt.show()

plt.imshow(np.reshape(x2, (28,28)), interpolation='nearest')
plt.show()
plt.imshow(np.reshape(y2, (28,28)), interpolation='nearest')
plt.show()


plt.imshow(np.reshape(d1, (28,28)), interpolation='nearest')
plt.show()
plt.imshow(np.reshape(d2, (28,28)), interpolation='nearest')
plt.show()
