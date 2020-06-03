from math import *

def newtonIterationFunction(x): 
    return x - (((-8*exp(1-x)+7/x)) / (8*exp(1-x)-7/x**2))
 

def function(x): 
    return -8*exp(1-x)+7/x

x = 1.6
c = 1
xold = 0
fc = 1

for i in range(1000):
    print "Iteraciones: ",str(i),"Valor aproximado: ", str(x), "Intervalo", str(c), "f(c)", str(fc)
    c = abs(x - xold)
    fc = function(x)
    xold = x
    x = newtonIterationFunction(x) 
    if (abs(c) < 0.000000005) :
        print ("Solucion encontrada!")
        break