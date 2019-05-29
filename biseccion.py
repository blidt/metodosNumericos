from math import *
 

lInferior = 1.0
lSuperior = 2.0
tol = 0.01
maxIter = 5
 
def f(x):
    return x**3 -2.0
 
i = 0
fa = f(lInferior)
fb = f(lSuperior)

while i <= maxIter:
    pMedio = (lInferior + lSuperior)/2
    fc = f(pMedio)
    print ("La raiz buscada es: %.4f" %pMedio, "con " + str(i) + " iteraciones.")
    if (fc == 0) or abs(fc) < tol:
        
        break
    
    i = i +1
    if (fa*fc > 0):
        lInferior=pMedio
        fa = f(lInferior)

    else:
        lSuperior = pMedio
        fb = f(lSuperior)