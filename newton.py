from math import *

def newtonIterationFunction(x): 
    return x - ((x+exp(-x)-1.5) / (1-exp(-x)))

 
x = -1.0

for i in range(5):
    print "Iteraciones: ",str(i),"Valor aproximado: ", str(x)
    xold = x
    x = newtonIterationFunction(x) 
    if (abs(x - xold)<0.01) :
        print "Solucion encontrada!"
        break