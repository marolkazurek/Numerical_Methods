import numpy as np
import math
import matplotlib.pyplot as plt

f1 = lambda x : x / (4 * x**2 + 1)
f2 = lambda x, k : math.pow(x, k)
f3 = lambda x : math.pow(math.sin(x), 2)
f4 = lambda x : math.pow(math.sin(x), 4)
a = 0
b = 2
n = 20
#########################################
def leggauss(a, b, n, f):
    x, w = np.polynomial.legendre.leggauss(n)
    # konwersja z [-1, 1] do [a, b]
    x = .5 * (x + 1) * (b - a) + a
    w *= .5 * (b - a)
    c = 0.
    for i in range(1, n):
        c += w[i] * f(x[i])
    # g = sum(w * f(c1)) * .5*(b - a)
    return c
#########################################
def c1a(x1, x2, a, c):
    B = ( np.log(a**2 * x2**2 + c**2) / (2 * a**2) )
    A = ( np.log(a**2 * x1**2 + c**2) / (2 * a**2) )
    return B - A
#########################################
def laggauss(k, n, f):
    x, w = np.polynomial.laguerre.laggauss(n)
    c = 0.
    for i in range(n):
        c += w[i] * f(x[i], k)
    return c
#########################################
def c2a(k):
    return math.factorial(k)
#########################################
def hermgauss(n, f):
    x, w = np.polynomial.hermite.hermgauss(n)
    c = 0.
    for i in range(n):
        c += w[i] * f(x[i])
    return c
#########################################
N = [n for n in range(2, 21)]
N = np.array(N, dtype = int)
print('n', N)
C1 = []
for _n in N:
    C1.append(leggauss(a, b, _n, f1))       
C1a = []
for _n in N:
    C1a.append(c1a(0, 2, 2, 1))
C1 = np.array(C1)
C1a = np.array(C1a)

#########################################

for _n in N:
    x, w = np.polynomial.legendre.leggauss(_n)
    # print('n: ', _n, 'sum :', sum(w))

# b)
print(leggauss(a, b, n, f1))
print(c1a(0, 2, 2, 1))
plt.figure()
_x = np.arange(a, b, .01)
plt.plot(_x, f1(_x), color = (1, 0, 0))
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
# plt.show()

###########################################
# 2
k = 5
i21 = []
i22 = []
for _n in N:
    i21.append(laggauss(k, _n, f2))
    i22.append(laggauss(10, _n, f2))
i21 = np.array(i21)
i22 = np.array(i22)
i21a = math.factorial(k)
i22a = math.factorial(10)
#
plt.figure()
plt.plot(N, abs(i21 - i21a), 'o-', color = ((133/255, 154/255, 101/255)), label = r'$k = 5$')
plt.plot(N, abs(i22 - i22a), 'o-', color = ((122/255, 101/255, 154/255)), label = r'$k = 10$')
print('abs(i21 - i21a)',abs(i21 - i21a), '\nabs(i22 - i22a)', abs(i22 - i22a))
plt.xlabel(r'iteracja $n$')
plt.ylabel(r'$|c_1 - c_{1,a}|$')
# plt.yscale('log')
plt.grid()
plt.legend()
##################################################################
locator = matplotlib.ticker.MultipleLocator(2)
plt.gca().xaxis.set_major_locator(locator)
formatter = matplotlib.ticker.StrMethodFormatter("{x:.0f}")
plt.gca().xaxis.set_major_formatter(formatter)
##################################################################
#
plt.figure()
x = np.arange(0, 8, .01)
plt.plot(x, x**5, '-', color = ((133/255, 154/255, 101/255)), label = r'$k = 5$')
plt.legend()
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.figure()
plt.plot(x, x**10, '-', color = ((122/255, 101/255, 154/255)), label = r'$k = 10$')
plt.legend()
plt.grid()
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')

for _n in N:
    x, w = np.polynomial.laguerre.laggauss(_n)
    # print('n: ', _n, 'sum :', sum(w))


############################################################
# 3
c_dok = 0.1919832644
N = np.arange(2, 16)
i2 = []
i1 = []
for _n in N:
    i1.append(hermgauss(_n, f3)) 
    i2.append(hermgauss(_n, f4))
print(len(i1))
i1 = np.array(i1)
i2 = np.array(i2)
i = i1 * i2
plt.figure()
plt.plot(N, abs(i - c_dok), '-o', color = (1,0,0))
plt.grid()
plt.yscale('log')
plt.xlabel(r'$n$')
plt.ylabel(r'$|c_2 - c_{dok}|$')

######################################################