''' Metodo de la Secante para encontar la raiz de una funcion
    x= x1-f(x1)*(x1-x0)/(f(x1)-f(x0)). Entrada de datos: xo, x1,
    tolerancia,numero de iteraciones maximo y funcion
'''    
def Secante(x0,x1,tol,N,f):
    print "Iteracion     x_n+1     xn     x_n-1     f(xn)"
    i=1
    h= 0.00001   #delta x para calcular la derivada de f(x)
    while i<=N:
        x= x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))  
        fx = f(x)

        print "%.4f" %i, "%.4f" %x,"    %.4f" %x0,"    %.4f" %x1, "    %.4f" %fx
        if (abs(x-x1)<tol or f(x)==0.0):
            return x
        i=i + 1
        x0=x1    # redefinir x0
        x1=x     #redefinir x1

    print('El metodo fracaso despues de %d iteraciones' %N)
    
from math import *     #just in case
    
    # Datos para corrida de ejemplo
    
f=lambda x: x**3-2
x0=1.0
x1=2.0
tol=0.01
N=5

x=Secante(x0,x1,tol,N,f)

print'La solucion es: ',x