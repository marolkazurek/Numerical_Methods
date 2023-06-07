import math
import matplotlib.pyplot as plt
import numpy as np
# m=5 #0 1 5
# k=5 #1 1 5
# I=2 pi 56.363569
a=0
b=math.pi


# N=201 #11 21 51 101 201
# h=(b-a)/N

############################################
def fun(x,m,k):
    return (x**m)*math.sin(k*x)

############################################
def S(i,m,k,h):
    title = r'$ m = %(m)d, k = %(n)d $' % {'m': m, 'n': k}
    result=(1/3)*h*(fun(a+i*h,m,k)+4*fun(a+(i+1)*h,m,k)+fun(a+(i+2)*h,m,k))
    plt.figure(figsize=(6, 4), dpi=80)
    plt.title(title)
    plt.xlabel(r'iteracja $i$')
    plt.ylabel(r'$I$')
    plt.grid()
    plt.plot([x for x in range(len(result))], result, 'o-', color = (1,0,0))
    plt.savefig('i' + title + '.png')
    return result
############################################
def I(n1,m,k):
    return sum(((-1)**i)*(((k*b)**(2*i+m+2))/((k**(m+1))*math.factorial(2*i+1)*(2*i+m+2)))-((-1)**i)*(((k*a)**(2*i+m+2))/((k**(m+1))*math.factorial(2*i+1)*(2*i+m+2))) for i in range(n1))
############################################
# val1=[]
# val2=[]
# # suma=0
# # for i in range(0,N,2):
# #     suma+=S(i)
# #     val1.append(suma)
# # print(val1)
# for i in range(30):
#     val2.append(I(i))
# print(val2)
# print(val2[-1]-val1[-1])
############################################

M_K = [(0,1),(1,1),(5,5)]
N = [11, 21, 51, 101, 201]

for m, k in M_K:
    l=[]
    for i in range(30):
        l.append(I(i,m,k))
    integ = []
    for n in N:
        h=(b-a)/n
        integ.append(sum(S(i,m,k,h) for i in range(0,n,2)))
    print("calka obliczona numerycznie", integ[-1])
    print("calka obliczona dokladnie", l[-1])
    print("abs c - i", np.abs(integ[-1] - l[-1]))
    plt.figure(figsize=(6, 4), dpi=80)
    title = r'$ m = %(m)d, k = %(n)d $' % {'m': m, 'n': k} 
    plt.title(title)
    plt.grid()
    plt.yscale('log')
    plt.xlabel(r'liczba węzłów $n$')
    plt.ylabel(r'$|C-I|$') 
    wykres2 = np.array(l)
    integ = np.array(integ)
    plt.plot([k for k in N], np.abs(integ - l[-1]), 'o-', color = (1,0,0))
    plt.legend()
    plt.savefig('c' + title + '.png')
plt.show()