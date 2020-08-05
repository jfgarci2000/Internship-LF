# function to get s

import numpy as np
import math



def get_s(x, y):
    s = np.ones(len(x))
    list = []
    rx_list = []
    ry_list = []
    for i in range(len(x)):
        if x[i] < 0 and y[i] < 0:
            s[i]=0
        if x[i] > 0 and y[i] < 0:
            r = (x[i] ** 2) / ((x[i] - y[i]) ** 2)
            rx_list.append((r, i))
        if x[i] < 0 and y[i] > 0:
            r = (y[i] ** 2) / ((x[i] - y[i]) ** 2)
            ry_list.append((r, i))

    rxlen = len(rx_list)+1
    rylen = len(ry_list)+1

    sarray = np.ones((rxlen,rylen,len(s)))
    for i in range(len(s)):
        if s[i] == 0:
            for k in range(rxlen):
                for l in range(rylen):
                    sarray[k][l][i] = 0

    rx = sorted(rx_list, key=lambda x: x[0])
    ry = sorted(ry_list, key=lambda x: x[0])
    for k in range(rxlen):
        for j in rx[0:k]:
            for l in range(rylen):
                sarray[k][l][j[1]] = 0
    for l in range(rylen):
        for j in ry[0:l]:
            for k in range(rxlen):
                sarray[k][l][j[1]] = 0
    return rx, ry, sarray


def get_g(x, y, s):
    a_square = 0
    b_square = 0
    c_square = 0

    for i in range(len(s)):
        if s[i] == 1:
            c_square += ((x[i] - y[i])**2)
        else:
            if x[i] >= 0:
                a_square += (x[i]**2)
            if y[i] >= 0:
                b_square += (y[i]**2)

    if a_square >= (b_square + c_square):
        t_square = a_square
    elif b_square >= (a_square + c_square):
        t_square = b_square
    else:
        t_square = (c_square/4) + (((a_square - b_square)**2) / (4*c_square)) + ((a_square + b_square) / 2)

    return math.sqrt(t_square)


def get_h(x, y):
    (rx, ry, sarray) = get_s(x, y)
    shape = np.shape(sarray)
    array = np.ndarray(shape[0:2])
    for k in range(shape[0]):
        for l in range(shape[1]):
            array[k, l] = get_g(x, y, sarray[k, l, :])
    print(array)
    print(rx)
    print(ry)
    return min(np.nditer(array))


rng = np.random.default_rng()
y = rng.standard_normal(10)
x = rng.standard_normal(10)

print(x)
print(y)
print(get_h(x, y))



