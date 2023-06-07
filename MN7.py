import math
#########################
def fun(x):             #
    return 1/(1+x**2)   #
#########################
def product(x,j):
    prod=1
    for i in range(j-1):
        prod*=(j-x[i])
    return prod
###########################################################
def right_tab(n,f,x):                                     #
    for j in range(1,n+1):                                #
        for i in range(j,n+1):                            #
            f[i][j]=(f[i][j-1]-f[i-1][j-1])/(x[i]-x[i-j]) #
    return f                                              #
###########################################################
def Chebyshev(i,n):
    return 0.5 * ((a - b) * math.cos(math.pi * (2 * i + 1) / (2 * n + 2) + (a + b)))
###########################################################
def interpol(n,f,x_i):

    helper=f[0]
    tmp=sum(f[j]*product(x,j) for j in range(1,n+1))

    return tmp+helper 

N=[5,10,15,20]
a=-5
b=5
###########
for n in N:
    d_x=(b-a)/n
    x=[a+i*d_x for i in range(n+1)]
    xc=[Chebyshev(i,n) for i in range(n+1)]
################################
    A=[[fun(x[j]) if i==0 else 0 for i in range(n+1)] for j in range(n+1)]
    Ac=[[fun(xc[j]) if i==0 else 0 for i in range(n+1)] for j in range(n+1)]
    A=right_tab(n,A,x)
    Ac=right_tab(n,Ac,x)
    f=[A[i][j] for i in range(n+1) for j in range(n+1) if i==j]
    fc=[Ac[i][j] for i in range(n+1) for j in range(n+1) if i==j]
    print(n, "f(x)\n", f)
    print(interpol(n,f,x))
    print(n, "f(x)\n",fc)
    print(interpol(n,fc,xc))

