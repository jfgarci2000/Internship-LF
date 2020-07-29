# function to get s

import numpy as np

s = []
def get_s(x, y, s):
    k = []
    l = []
    for i in range(len(x)):
        if x[i] >= 0:
            if y[i] >= 0:
                s.append((x[i], y[i]))

            else:
                r = (x[i]**2) / ((x[i] - y[i])**2)
                k.append((x[i], y[i]))
                if r > 0.5:
                    s.append((x[i], y[i]))

        else:
            if y[i] >= 0:
                r = (y[i] ** 2) / ((x[i] - y[i]) ** 2)
                l.append((x[i], y[i]))

                if r > 0.5:
                    s.append((x[i], y[i]))

    return s


x = np.array([1, 1, -1, -1, 5, -1])
y = np.array([1, -1, 1, -1, -1, 5])

print(get_s(x, y, s))

