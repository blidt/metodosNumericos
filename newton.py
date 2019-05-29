import math

def newtonIterationFunction(t): 
    return t - ((t**3 -2) / (3*t**2))

 
x = 1
 
for i in range(5):
    print "Iteraciones: ",str(i),"Valor aproximado: ", str(x)
    xold = x
    x = newtonIterationFunction(x) 
    if abs(x - xold)<0.01:
        print "Solucion encontrada!"
        break