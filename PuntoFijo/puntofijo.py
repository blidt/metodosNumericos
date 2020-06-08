from math import *


def gx(x):
    return (-exp(x)+x +4)/x

def puntofijo(a,tol, n = 20):

    i = 1
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tol and i<=n):
        print "El punto fijo es ",b," despues de ",i," iteraciones"
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i+1
    respuesta = b

    return(respuesta)



# PROCEDIMIENTO
respuesta = puntofijo(1,10**-25)