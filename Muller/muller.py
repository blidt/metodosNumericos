def MullerM(f,p0,p1,p2,tol,maxIter):
    from numpy.lib.scimath import sqrt

    p0 = p0
    p1 = p1
    p2 = p2
    f0 = f(p0)
    f1 = f(p1)
    f2 = f(p2)
    f3 = 0
    i = 0
    while i<=maxIter:
        c = f2
        b = ((p0-p2)**2 *(f1-f2)-(p1-p2)**2 *(f0-f2))/((p0-p2)*(p1-p2)*(p0-p1))
        a = ((p1-p1)*(f0-f2) - (p0-p2)*(f1-f2))/((p0-p2)*(p1-p2)*(p0-p1))
        p3 = p2 - 2*c/(b+(b/abs(b))*sqrt(b**2 -4*a*c))
        f3 = f(p3)
        print ("Pn =  ", p3, "   f(Pn) =  ", f3)
        if abs(p3-p2)<tol:
            return p3
        p0 = p1
        p1 = p2
        p2 = p3
        f0 = f(p0)
        f1 = f(p1)
        f2 = f(p2)
        i = i+1
    print ("No se encontró la raiz")
    
def f(x):
    import math
    fx = x -math.sin(x)
    return fx

MullerM(f,-0.1,-0.01,0.001,0.00001,100)