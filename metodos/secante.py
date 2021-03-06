from math import *

def fx(x):
    respuesta = (1 + 85.6409/(sqrt(450)*x *(x + 0.2590273)))*(x - 0.2590273) - (0.08206*450)
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

secante(30, 40, 0.000000005)