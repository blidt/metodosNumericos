#Actual Values: BLACK LINE
#Lagrange Calc: RED LINE
#Vander Calc:   RED "+"

#Data used based on example at:
    #http://jayemmcee.wordpress.com/lagrange-polynomial-interpolation/
#Required module Vandermonde can be found at:
    #http://pastebin.com/gWfYcj0W

import numpy as np
import Vandermonde as V
import matplotlib as mpl
mpl.use("TKAgg")
import matplotlib.pylab as plt
plt.ion()

#Actual function res
R=400
#Num of Interp pts
n=5
#Num of estimated poly plot pts
E=250
#Endpoints
a= -1; b=1
#Function to compare
x = lambda n: np.linspace(a,b,n)
f = lambda x: np.cos(np.sin(np.pi*x))

def PolyVander(n,E,x,f):
    data = zip(x(n),f(x(n)))
    Vander = V.VanderInterp(data)
    print "Vander Values:   ",list(Vander)
    return V.toVector(Vander, x(E))

plt.clf()
#Actual Values
plt.plot(x(R), f(x(R)), 'k')

#Lagrange Coeffs as calculated at:
    #http://jayemmcee.wordpress.com/lagrange-polynomial-interpolation/

#c ~ 0.540302305868, for convenience of typing
c = f(0.5)
co = [3, 0, -(16-16*c), 0, (16-16*c)]
co[:] = [i/3.0 for i in co]
Lx = [0.0] * E
for i in xrange(E):
    Lx[i] = co[0] + co[1]*x(E)[i] + co[2]*(x(E)[i])**2
    Lx[i] += co[3]*(x(E)[i])**3 + co[4]*(x(E)[i])**4
plt.plot(x(E), Lx, 'r')
print "Lagrange Values: ",co

#Estimated Value
    #Simply to demonstrate that Vandermonde
    #And Lagrange_Pts are same values
plt.plot(x(E),PolyVander(n,E,x,f),'r+')