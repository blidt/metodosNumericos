from math import *

def fx(x):
    respuesta = return x-cos(x)
    return round(respuesta,4)


def posicionfalsa(a,b,tol):
    fa = fx(a)
    fb = fx(b)
    c = b - fb*(a-b)/(fa-fb)    
    i = 1
    tramo = abs(c-a)
    fc = fx(c)
    print "Iteracion     a     b     c    f(a)   f(b)     f(c)"
    for i in range (5):
        print ("" %i, "%.4f" %a,"    %.4f" %b,"    %.4f" %c, "    %.4f" %fa,"    %.4f" %fb,"    %.4f" %fc)
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

    print "La raiz buscada es: %.4f" %c, "con " + str(5) + " iteraciones."    

posicionfalsa(0.0,2.0,0.01)