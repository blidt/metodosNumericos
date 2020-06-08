from math import *

def fx(x):
    return -8*exp(1-x)+7/x


def posicionfalsa(a,b,tol):
    fa = fx(a)
    fb = fx(b)
    c = b - fb*(b-a)/(fb-fa)    
    i = 0
    tramo = abs(c-a)
    fc = fx(c)
    print ("Iteracion     a     b     c    f(a)   f(b)     f(c)")
    for i in range (1000):
        print ("%.0f" %i, "%.10f" %a,"    %.10f" %b,"    %.10f" %c, "    %.10f" %fa,"    %.10f" %fb,"    %.10f" %fc)
        fc = fx(c)
        
        i = i+1
        fc = fx(c)
        
        if (fc==0.0 or tramo < tol):
            break
        if (fa*fc < 0 ):
            a=c
            fa=fc
        else:
            b=c
            fb=fc
        c = b - fb*(a-b)/(fa-fb)
        tramo = abs(fc)

    print ("La raiz buscada es: %.10f" %c, "con " + str(i) + " iteraciones.")    

posicionfalsa(1.6,1.7,0.0000000005)