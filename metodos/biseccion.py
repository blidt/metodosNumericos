from math import *
 

lInferior = 0.1
lSuperior = 1
tol = 10**-15
maxIter = 100
 
def f(x):
    return 230*x**4 +18*x**3 + 9*x**2 -221*x -9
 
i = 0
fa = f(lInferior)
fb = f(lSuperior)
 
while i <= maxIter:
    pMedio = (lInferior + lSuperior)/2
    fc = f(pMedio)
 
    if (fc == 0.0) or abs(fc) < tol:
        print "La raiz buscada es: %.4f" %pMedio, "con " + str(i) + " iteraciones."
        break
    
    i = i +1
    if (fa*fc > 0):
        lInferior=pMedio
        fa = f(lInferior)

    else:
        lSuperior = pMedio
        fb = f(lSuperior)