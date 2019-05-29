import math

def newtonIterationFunction(t): 
    return t - (math.exp(x)  + 3*x + 5.5 ) / (3 + math.exp(x))

 
x = 10
 
for i in range(100):
    print "Iteraciones: ",str(i),"Valor aproximado: ", str(x)
    xold = x
    x = newtonIterationFunction(x) 
    if abs(x - xold)<10**(-30):
        print "Solucion encontrada!"
        break