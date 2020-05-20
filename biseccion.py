from math import *
 

lInferior = -1.0
lSuperior = 0.0
tol = 0.01
maxIter = 5
 
def f(x):
    return x+exp(-x)-1.5
 
i = 1
fa = f(lInferior)
fb = f(lSuperior)
print "Iteracion     a     b     c     f(c)"
while i <= maxIter:
    pMedio = (lInferior + lSuperior)/2
    fc = f(pMedio)
    print "%.4f" %i, "%.4f" %lInferior,"    %.4f" %lSuperior,"    %.4f" %pMedio, "    %.4f" %fc
    if (fc == 0) or abs(fc) < tol:
        print "La raiz buscada es: %.4f" %pMedio, "con " + str(i) + " iteraciones."
        break
    
    i = i +1
    if (fa*fc > 0):
        lInferior=pMedio
        fa = f(lInferior)

    else:
        lSuperior = pMedio
        fb = f(lSuperior)