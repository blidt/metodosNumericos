''' Metodo de la Secante para encontar la raiz de una funcion
    x= x1-f(x1)*(x1-x0)/(f(x1)-f(x0)). Entrada de datos: xo, x1,
    tolerancia,numero de iteraciones maximo y funcion
'''    
def Secante(x0,x1,tol,N,f):

    print(0,x0,x1)
    i=1
    h= 0.00001   #delta x para calcular la derivada de f(x)
    while i<=N:
        x= x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))  

        print(i,x)
        if abs(x-x1)<tol:
            return x
        i=i + 1
        x0=x1    # redefinir x0
        x1=x     #redefinir x1

    print('El metodo fracaso despues de %d iteraciones' %N)
    
import math     #just in case
    
    # Datos para corrida de ejemplo
    
f=lambda x: x**3 -2
x0=1
x1=2
tol=0.01
N=5

x=Secante(x0,x1,tol,N,f)
print()
print('La solucion es: ',x)