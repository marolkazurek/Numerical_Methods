import math
import random
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import cmath
#############
k=10
N=2**k
w=2*(2*math.pi)/N
#########################################################
def fun(x):
    return math.sin(w*x)+math.sin(2*w*x)+math.sin(3*w*x)
#########################################################
f=[fun(i) for i in range(N)]
f_szum=[f[i]+random.uniform(-0.9999999999999999,1) for i in range(N)]

p1=plt.figure()
p2=plt.figure()
p3=plt.figure()
p4=plt.figure()
x=[i for i in range(N)]
ax1=p1.add_subplot(1,1,1)
ax2=p2.add_subplot(1,1,1)
ax3=p3.add_subplot(1,1,1)
ax4=p4.add_subplot(1,1,1)

ck=fft(f_szum)
ax1.plot(ck.real, color='tab:blue',label=r'$real FFT$')
ax1.plot(ck.imag, color='tab:red',label=r'$img FFT$')
ax1.set_xlabel('x')
ax1.set_ylabel('$c_k$')
ax1.legend()

ax2.plot(x,f_szum,color='tab:red',label=r'$zaburzony$')
ax2.plot(x,f, color='tab:blue',label=r'$splot$')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.legend()

prog=[max(abs(ck))/2 for i in x]

ax3.plot(abs(ck), color='tab:blue',label=r'$|FFT|$')
ax3.plot(x,prog,color='tab:red',label=r'$prog dyskryminacji$')
ax3.set_xlabel('x')
ax3.set_ylabel('$c_k$')
ax3.legend()

for i in range(N):
    if abs(ck[i])<max(abs(ck))/2:
        ck[i]=0

f_new=ifft(ck)
ax4.plot(x,f, color='tab:blue',label=r'$splot$')
ax4.plot(x,f_new,color='tab:red',label=r'$niezaburzony$')
ax4.set_xlabel('x')
ax4.set_ylabel('f(x)')
ax4.legend()

##################################


plt.show()