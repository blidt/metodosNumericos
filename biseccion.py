from math import *
 

a = float(input('Ingrese el valor a:'))
b = float(input('Ingrese el valor b:'))
tol = float(input('Ingrese la tolerancia:'))
maxIter = 1000000
 
def f(x):
    return -8*exp(1-x)+7/x
 
i = 1
fa = f(a)
fb = f(b)
print ("Iteracion     a     b     c     f(c)")
while i <= maxIter:
    pMedio = (a + b)/2
    fc = f(pMedio)
    print( "%.7f" %i, "%.7f" %a,"    %.7f" %b,"    %.7f" %pMedio, "    %.7f" %fc)
    if (fc == 0) or abs(b - a) < tol:
        print ("La raiz buscada es: %.7f" %pMedio, "con " + str(i) + " iteraciones.")
        break
    
    i = i +1
    if (fa*fc > 0):
        a=pMedio
        fa = f(a)

    else:
        b = pMedio
        fb = f(b)