import numpy as np 

def jacobi(A, b, x_init, epsilon=10e-2, max_iterations=300):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    for i in range(max_iterations):
        D_inv = np.diag(1 / np.diag(D))
        x_new = np.dot(D_inv, b - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < epsilon:
            return x_new
            break
        x = x_new
        print("i=", i)
    return x

A = np.array([
    [1, 0, -2],
    [-1/2, 1, -1/4],
    [1, -1/2, 1]
])
b = np.array([0.2, -1.425, 2])

x_init = np.zeros(len(b))
x = jacobi(A, b, x_init)

print('x:', x)
print('computed b:', np.dot(A, x))
print('real b:', b)