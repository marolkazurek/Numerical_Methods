import random
import math
import numpy as np
########
x_min=-4
x_max=4
n=201
x_0=2.
m=10 #30 50
#################
d=(x_max-x_min)/16
Y=random.random()
C=(Y-0.5)/5
x_i=[x_min+(i)*d for i in range(n)]
#####################################

A=[[0 for i in range(n) ] for i in range(m+2)]
for j in range(n):
    A[0][j]=0.0
    A[1][j]=1.0

############################################
def fun(x):
    return math.sin((14*math.pi*x)/(x_max-x_min))*(math.exp(-((x-x_0)**2)/(2*d**2))+math.exp(-((x+x_0)**2)/(2*d**2)))
############################################
def beta(j):
    if j==1:
        return 0
    else:
        return sum(x_i[i]*A[j-1][i]*A[j][i] for i in range(n))/sum((A[j-1][i])**2 for i in range(n))
############################################
def alpha(j):
    return sum(x_i[i]*(A[j-1][i])**2 for i in range(n))/sum((A[j-1][i])**2 for i in range(n))
############################################

for i in range(1,m+1):
    alfa = alpha(i+1)
    bet  = beta(i)
    for j in range(n):
      A[i+1][j]=(x_i[j]-alfa)*A[i][j]-bet*A[i-1][j]
      if(j == 0):
        normalize=A[i+1][0]
      A[i+1][j]=A[i+1][j]/normalize

############################################
def funszum(x):
    return fun(x)+C
############################################
def bk(k):
    return Ck(k)/Sk(k)
############################################
def Ck(k):
    return sum(fun(x_i[i])*A[k][i] for i in range(n))
############################################
def Sk(k):
    return sum((A[k][i])**2 for i in range(n))
############################################
def F(x):
    return sum(bk(k)*A[k][x] for k in range(2,m+2))
############################################

ideal=[funszum(i) for i in np.arange(-4,4,0.01)]
orginal=[fun(i) for i in np.arange(-4,4,0.01)]
approx={x_i[i]:F(i) for i in range(201)}
print(ideal)
print(orginal)
print(approx)