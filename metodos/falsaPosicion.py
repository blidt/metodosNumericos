from math import *

def fx(x):
    respuesta = return x**3 -2.0
    return round(respuesta,4)


def posicionfalsa(a,b,tol):
    fa = fx(a)
    fb = fx(b)
    c = b - fb*(a-b)/(fa-fb)

    i = 0
    tramo = abs(c-a)
    fc = fx(c)
    while (tramo > tol or i < 100):
        i = i+1
        fc = fx(c)
        if (fc==0.0):
            break
        if (fa*fc < 0):
            a=c
            fa=fc
        else:
            b=c
            fb=fc
        c = b - fb*(a-b)/(fa-fb)
        tramo = abs(c-a)
        
    print "La raiz buscada es: %.4f" %c, "con " + str(i) + " iteraciones."    
    return(0)

posicionfalsa(0.8,1,10**-15)