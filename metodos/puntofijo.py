from math import *
from decimal import Decimal, localcontext

def gx(x):
    with localcontext() as ctx:
        ctx.prec = 100
        respuesta = Decimal(0) 
        respuesta = (x**3 -1.2)/(0.9)
    return respuesta

def puntofijo(a,tol, n = 15):

    i = 1
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tol and i<=n):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i+1
    respuesta = b

    return(respuesta)


a = 0 ; b = 1
tol = 0.001
tramos = 101

# PROCEDIMIENTO
respuesta = puntofijo(1.5,10**-2)

# SALIDA
print(respuesta)