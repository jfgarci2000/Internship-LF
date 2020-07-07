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
x = np.reshape(v[0][0],(784,))
y = np.reshape(v[1][0],(784,))
(t, x1, y1, d1) = (compute_t.get_t(v[0][0], v[1][0], np.identity(784)))
# result = (compute_t.get_infinity(x, y, np.identity(784)))
# print(sp.euclidean(v[0][0], v[1][0]))
# print(result)

net = network.Network([784, 30, 10])



# net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
for i in range(30):
    d = np.load('output {}.npy'.format(i))
    (t2, x2, y2, d2) = (compute_t.get_t(v[0][0], v[1][0], d))
    print(t2)
#print(net.weights)


# result2 = (compute_t.get_infinity(x, y, q))
# print(result2)


from matplotlib import pyplot as plt
plt.gray()
plt.imshow(np.reshape(d[0],(28,28)), interpolation='nearest')
plt.show()
# plt.imshow(np.reshape(x, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(x1, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(y, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(y1, (28,28)), interpolation='nearest')
# plt.show()

# plt.imshow(np.reshape(x2, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(y2, (28,28)), interpolation='nearest')
# plt.show()


# plt.imshow(np.reshape(d1, (28,28)), interpolation='nearest')
# plt.show()
# plt.imshow(np.reshape(d2, (28,28)), interpolation='nearest')
# plt.show()
