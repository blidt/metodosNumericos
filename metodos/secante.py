from math import *

def fx(x):
    respuesta = -8*exp(1-x)+7/x
    return respuesta


def secante(a,b,tol):
    fa = fx(a)
    fb = fx(b)
    c = b - fb*((b-a)/(fb-fa))    
    i = 1
    error = abs(b-a)
    fc = fx(c)
    print ("Iteracion          a                    b                 c                   f(c)                   error ")
    for i in range (1000):
        c = b - (fb*(b-a)/(fb-fa))
        fc = fx(c)
        print ("%.0f" %i, "          %.12f" %a,"          %.12f" %b,"    %.12f" %c, "    %.12f" %fc, "        %.12f" %error)
        i = i+1
        if (fc==0.0 or abs(b-a) < tol):
            break

        a = b
        b = c
        fa = fx(a)
        fb = fx(b)
        
        error = abs(b-a)

    print ("La raiz buscada es: %.12f" %c, "con " + str(i) + " iteraciones.")

secante(1.6, 1.7, 0.0000000005)