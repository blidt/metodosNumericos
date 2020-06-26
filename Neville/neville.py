from sympy import symbols, init_printing, lambdify, horner, expand, pprint
import numpy as np
from numpy import zeros, diag

def polneville(x, y, x0):
    Q = np.zeros((len(x), len(x)), dtype=float)
    for k in range(0, len(x)):
        Q[k][0] = y[k]

    for i in range(1, len(x)):
        for j in range(1, i + 1):
            Q[i][j] = ((x0-x[i-j])*Q[i][j-1]-(x0-x[i])*Q[i-1][j-1])/(x[i]-x[i-j])

    return [Q[-1][-1], np.diag(Q, 0)]

datosx = np.array([0, 1, 2, 4, 5], dtype=float)
datosy = np.array([0, 1, 1.414213562373095048, 2, 2.236067977499789696409173668], dtype=float)

interpolar = 3
valorN = polneville(datosx, datosy, interpolar)[0]
pprint('Para {0} obtenemos {1} con Neville. '.format(interpolar, valorN))