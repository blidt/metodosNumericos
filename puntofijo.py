from  __future__  import division
from  scipy       import *
from  matplotlib.pyplot import *

def f(g,x0):
    for n in range(1,100):
        x1=g(x0)
        if abs(x1-x0)<10**(-1):
            print(x1)
            
            break
        else:
            x0=x1
            print "Iteraciones: ",str(n),"Valor aproximado: ", str(x1)
    return x1
    
def ga(x):
    return (1.52)/(x**2-0.9)
   
y=f(ga,1)
print "Valor aproximado: ", str(y)