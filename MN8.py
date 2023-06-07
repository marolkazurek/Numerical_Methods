import math
import matplotlib.pyplot as plt
import numpy as np
#########################################
a=-5
b= 5
x=[i for i in range(a,b+1)]
y1=[func1(i) for i in x]
y2=[func2(i) for i in x]
#########################################
def func1(x):
    return 1/(1+x**2)
#########################################
def func2(x):
    return math.cos(2*x)
#########################################
def sec_der(f,x,d_x):
    return (f(x - d_x) - 2 * f(x) + f (x + d_x)) / (d_x * d_x)
#########################################
def mat(u,l,n):
    M=[[1 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j:
                M[i][j]=2
            elif i==j and (i==0 or i==(n-1)): 
                M=[i][j]=1
            elif i==(j-1):
                M[i][j]=u[i-1]
            elif i==(j+1):
                M[i][j]=l[i-1]
            else:
                M[i][j]=0
    M[0][0]=1
    M[n-1][n-1]=1
    return M
            
#########################################
def A_i(i,y,h,m):
    return (((y[i]-y[i-1])/h[i])-(h[i]/6)*(m[i]-m[i-1]))
#########################################
def B_i(i,y,h,m):
    return y[i-1]-m[i-1]*((h[i]**2)/6)
#########################################
def s(xd,m,h,i,y):
    return m[i-1]*((x[i]-xd)**3/(6*h[i]))+m[i]*((xd-x[i-1])**3/(6*h[i]))+A_i(i,y,h,m)*(xd-x[i-1])+B_i(i,y,h,m)
#########################################
def interpol(x,y):
    ############
    alpha   =0
    beta    =0
    d_x     =.01
    ############
    h=[x[i]-x[i-1] for i in range(1,len(x))]
    d=[(6/(h[i]+h[i+1]))*((y[i+1]-y[i])/h[i+1]-(y[i]-y[i-1])/h[i]) for i in range(1,len(h)-1)]
    l=[h[i+1]/(h[i]+h[i+1]) for i in range(len(h)-1)]
    u=[1-i for i in l]
    M=mat(u,l,10)
    # M=mat(u,l,5)
    # M=mat(u,l,8)
    # M=mat(u,l,21)
    ##################################################################
    plt.figure()
    x_fun_org = np.arange(a, b, d_x)
    y_fun_org = func1(x_fun_org)
    plt.plot(x_fun_org, y_fun_org, label = r"Wykres $f_1(x)$")
    plt.xlabel(r'x')
    plt.ylabel(r'y')

    plt.scatter(x, y, color = (1,0,0), label = 'węzły interpolacyjne')
        
    y_int = [s(x,M,h,y,i) for i in x_fun_org]
    plt.plot(x_fun_org, y_int, label = r'Funkcja interpolująca $s(x)$')
        
        
    plt.grid()
    plt.legend()
    
    #########second derivate############
    # plt.figure()
    # plt.xlabel = (r'x')
    # plt.ylabel = (r'y')
    # _x = np.arange(a, b, d_x)
    # y_der = sec_der(func1(), _x, d_x)
    # y_der_points = sec_der(func1(), x, d_x)
    # plt.plot(_x, y_der,label = r'Wykres $\frac{d^2f}{dx^2}$')
    # plt.scatter(x, M, color = (1,0,0), label = r'Pochodne z równania $Am = d$')
    # plt.scatter(x, y_der_points, color = (10/255, 255/255, 84/255), label = r'Dokładniejsze pochodne')
    # plt.legend()
    # plt.grid()

#########################################

########
interpol(x,y1)
interpol(x,y2)
