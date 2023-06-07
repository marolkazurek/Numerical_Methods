import math
import random
import matplotlib.pyplot as plt
####################################
def f1(x):
    return 2*math.sin(x)+math.sin(2*x)+2*math.sin(3*x)
###############################################################
def f1rand(x):
    return 2*math.sin(x)+math.sin(2*x)+2*math.sin(3*x)+random.uniform(-0.5,0.5)
###############################################################
def f2(x):
    return 2*math.sin(x)+math.sin(2*x)+2*math.cos(x)+math.cos(x)
###############################################################
def f3(x):
    return 2*math.sin(1.1*x)+math.sin(2.1*x)+2*math.sin(3.1*x)
###############################################################
N=100
k=2*math.pi/N
x=[0+i*k for i in range(N)]
##############################
def A(j,f):
    if j==0:
        return (1/N)*sum(f(x[i]) for i in range(N))
    else:
        return (1/(N/2))*sum(f(x[i])*math.cos((2*math.pi*j*i)/N) for i in range(N))
#################################################################################
def B(j,f):
    return (1/(N/2))*sum(f(x[i])*math.sin((2*math.pi*i*j)/N) for i in range(N))
#################################################################################
def F(x,M_c,M_s,f):
    return (A(0,f)/2)+sum(A(j,f)*math.cos(j*x) for j in range(1,M_c))+sum(B(j,f)*math.sin(j*x) for j in range(1,M_s))

#1
p1=plt.figure()
p2=plt.figure()
p3=plt.figure()
p4=plt.figure()
p5=plt.figure()
p6=plt.figure()
p7=plt.figure()
ax1=p1.add_subplot(1,1,1)
ax2=p2.add_subplot(1,1,1)
ax3=p3.add_subplot(1,1,1)
ax4=p4.add_subplot(1,1,1)
ax5=p5.add_subplot(1,1,1)
ax6=p6.add_subplot(1,1,1)
ax7=p7.add_subplot(1,1,1)


fun1=[f1(i) for i in x]
z1=[F(i,5,5,f1) for i in x]
ax1.plot(x,fun1,'-o',color='tab:blue',label=r'$f_1(x)$')
ax1.plot(x,z1,color='tab:red',label=r'$F_1(x)$')
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.legend()

#2
fun2=[f2(i) for i in x]
z2=[F(i,5,5,f2) for i in x]
ax2.plot(x,fun2,'-o',color='tab:blue',label=r'$f_2(x)$')
ax2.plot(x,z2,color='tab:red',label=r'$F_2(x)$')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.legend()
#3
fun3=[f3(i) for i in x]
z3_1=[F(i,0,5,f3) for i in x]
z3_2=[F(i,5,5,f3) for i in x]
z3_3=[F(i,10,10,f3) for i in x]

ax3.plot(x,fun3,color='tab:blue',label=r'$f_3(x)$')
ax3.plot(x,z3_1,color='tab:red',label=r'$F_3(x)$')
ax3.set_xlabel('x')
ax3.set_ylabel('f(x)')
ax3.legend()
ax4.plot(x,fun3,color='tab:blue',label=r'$f_3(x)$')
ax4.plot(x,z3_2,color='tab:red',label=r'$F_3(x)$')
ax4.set_xlabel('x')
ax4.set_ylabel('f(x)')
ax4.legend()
ax5.plot(x,fun3,color='tab:blue',label=r'$f_3(x)$')
ax5.plot(x,z3_3,color='tab:red',label=r'$F_3(x)$')
ax5.set_xlabel('x')
ax5.set_ylabel('f(x)')
ax5.legend()
#4
fun4=[f1rand(i) for i in x]
z4_1=[F(i,5,5,f1rand) for i in x]
z4_2=[F(i,30,30,f1rand) for i in x]

ax6.plot(x,fun4,color='tab:blue',label=r'$f_1(x)$')
ax6.plot(x,z4_1,color='tab:red',label=r'$F_1(x)$')
ax6.set_xlabel('x')
ax6.set_ylabel('f(x)')
ax6.legend()

ax7.plot(x,fun4,color='tab:blue',label=r'$f_1(x)$')
ax7.plot(x,z4_2,color='tab:red',label=r'$F_1(x)$')
ax7.set_xlabel('x')
ax7.set_ylabel('f(x)')
ax7.legend()


plt.show()