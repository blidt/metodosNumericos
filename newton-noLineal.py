import numpy as np
from sympy import *



def jac():
    from sympy.abc import x, y, z

    X = Matrix([3*x-cos(x*y), x**2-81*(y+0.1)**2+sin(z)+1.06, rho**2])
    Y = Matrix([rho, phi])
    return X.jacobian(Y)





def Newton_system(F, J, x, eps):
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # l2 norm of vector
    iteration_counter = 0
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1

    # Here, either a solution is found, or too many iterations
    if abs(F_norm) > eps:
        iteration_counter = -1
    return x, iteration_counter