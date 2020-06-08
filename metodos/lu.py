import pprint
import scipy
import scipy.linalg   
import numpy as np
from math import sqrt

def sust_atras(A,b):
    n = len(b)
    x = np.zeros(n)
    for i in range(n-1, 0, -1):
        x[i] = A[i][i]/b[i]
        for j in range (i-1, 0, -1):
            A[i][i] += A[j][i]*x[i]

    print("Resultado usando sustutución hacia atrás: ")
    pprint.pprint(x)
def sust_adelante(L, y):
    for i in range(0, len(y)-1):
        for j in range(i+1, len(y)):
            factor = L[j][i]/L[i][i]
            for k in range(i,len(y)):
                L[j][k] = L[j][k] - factor*y[i]
            y[j] = y[j] - factor * y[j]
    print("Resultado usando la sustitución hacia adelante: ")
    pprint.pprint(y)

def cholesky(A):
    n = len(A)

    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): 
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
    print ("A:")
    pprint.pprint(A)

    print ("Cholevsky:")
    pprint.pprint(L)

A = scipy.array([ [1, 1, 1], [1, 2, 2], [1, 2,3]])
B = scipy.array([1,1,1])
C = np.transpose(B)
P, L, U = scipy.linalg.lu(A)

print ("A:")
pprint.pprint(A)

print ("P:")
pprint.pprint(P)

print ("L:")
pprint.pprint(L)

print ("U:")
pprint.pprint(U)

print ("El numero condicional es :" + str(np.linalg.cond(A)))
#sust_atras(U, C)
#sust_adelante(L,C)
cholesky(A)
