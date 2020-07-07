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


x_vector = np.array([0, 1])
y_vector = np.array([1, 1])
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
    aub = np.block([[v, np.eye(n), np.zeros((n,n))], [v, -(np.eye(n)) , np.zeros((n,n))], [v, np.zeros((n, n)), np.eye(n) ], [v, np.zeros((n,n)), -(np.eye(n)) ]])
    aeq = np.block([[np.zeros((m,1)), a, -a]])
    result = so.linprog(c, A_ub=aub, b_ub=bub, A_eq=aeq, b_eq=beq, options={"disp":True})



    return result
