import numpy as np
import time
import math

if __name__ == '__main__':

    for i in range(1, 7, 2):
        print(i)

    vektor = [5, 13, -1]
    for i in vektor:
        if i > 10:
            print('Larger than 10')
        elif i < 0:
            print('Negative value')
        else:
            print('Something else')

m = 50
n = 10
A = np.ones((m, n))
v = 2 * np.random.rand(1, n)

# Implementácia s použitím cyklov

for i in range(1, m):
    A[i, :] = A[i, :] - v

# Implementácia s použitím maticových operácií

A = np.ones((m, n)) - np.kron(np.ones((m, 1)), v)

# Implementácia s použitím cyklov

B = np.zeros((m, n))
for i in range(1, m):
    for j in range(1, n):
        if A[i, j] > 0:
            B[i, j] = A[i, j]

# Implementácia bez cyklov

B = np.zeros((m, n))
ind = np.where(A > 0)

B[ind] = A[ind]

tic = time.perf_counter()
x = [0]
for k in range(1, 1000000):
    x.append(0)
    x[k] = x[k - 1] + 5

toc = time.perf_counter()
duration = toc - tic

tic = time.perf_counter()
x = np.zeros(1000000)
for k in range(2, 1000000):
    x[k] = x[k - 1] + 5

toc = time.perf_counter()
duration = toc - tic


def myfunction(x):
    a = [-2, -1, 0, 1]
    y = a + x
    print(y)
    return y


def otherfunction(a, b):
    y = a + b
    z = a - b
    print(y, "", z)
    return y, z


a = np.array([1, 2, 3, 4])
b = myfunction(2 * a)
c, d = otherfunction(a, b)
print(c, d)