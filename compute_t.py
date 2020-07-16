# Code to compute t, Distance

import numpy as np

import scipy.linalg as sp
import scipy.optimize as so
import math



def get_t(x_vector, y_vector, a):

    matrix = a.dot(np.transpose(a))
    vector = a.dot(y_vector-x_vector)
    v_lamb = sp.solve(matrix, vector, assume_a='sym')
    d = 0.5*(np.transpose(a).dot(v_lamb))
    u = np.transpose(d).dot(d)

    t = math.sqrt(u)

    return t, x_vector + d, y_vector - d, d


# A matrix should be invertible (satisfying all the conditions of an invertible matrix)
a = np.array([[1, 0],
             [0, 1]])

# print(get_t(x_vector, y_vector, a))

def get_infinity(x_vector, y_vector, a):
    (m,n) = a.shape
    c= np.block([np.ones(1),np.zeros(2*n)])
    print(c.shape)
    bub = np.block([x_vector, -(x_vector), y_vector, -(y_vector)])
    print(bub.shape)
    beq = np.zeros(m)
    v= -np.ones((n,1))
    aub = np.block([[v, np.eye(n), np.zeros((n,n))], [v, -(np.eye(n)) , np.zeros((n,n))],
                    [v, np.zeros((n, n)), np.eye(n) ], [v, np.zeros((n,n)), -(np.eye(n)) ]])
    aeq = np.block([[np.zeros((m,1)), a, -a]])
    result = so.linprog(c, A_ub=aub, b_ub=bub, A_eq=aeq, b_eq=beq, options={"disp":True})

    return result


def relu(x_vector, y_vector):
    t = 0
    x_tilda = np.zeros(len(x_vector))
    y_tilda = np.zeros(len(y_vector))
    for i in range(len(x_vector)):
        if x_vector[i] >= 0:
            if y_vector[i] >= 0:
                dist = ((x_vector[i] - y_vector[i]) ** 2)/2
                x_tilda[i] = (x_vector[i] + y_vector[i])/2
                y_tilda[i] = x_tilda[i]
                t += dist

            else:
                dist = ((x_vector[i] - y_vector[i]) ** 2) / 2
                xdist = x_vector[i] ** 2
                if dist > xdist:
                    x_tilda[i] = 0
                    y_tilda[i] = y_vector[i]
                    t += xdist

                else:
                    x_tilda[i] = (x_vector[i] + y_vector[i]) / 2
                    y_tilda[i] = x_tilda[i]
                    t += dist

        else:
            if y_vector[i] >= 0:
                dist = ((x_vector[i] - y_vector[i]) ** 2) / 2
                ydist = y_vector[i] ** 2
                if dist > ydist:
                    y_tilda[i] = 0
                    x_tilda[i] = x_vector[i]
                    t += ydist
                else:
                    x_tilda[i] = (x_vector[i] + y_vector[i]) / 2
                    y_tilda[i] = x_tilda[i]
                    t += dist

            else:
                x_tilda[i] = x_vector[i]
                y_tilda[i] = y_vector[i]

    return x_tilda, y_tilda, t

x_vector = np.array([1, 1, -1, -1, 5, -1])
y_vector = np.array([1, -1, 1, -1, -1, 5])

print(relu(x_vector, y_vector))

