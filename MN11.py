import math
import random
from scipy.fft import fft,ifft

k=8 #10 ,12
N=2**k
T=1.0
t_max=3*T
dt=t_max/N
sig=T/20
w=2/math.pi/T
d=random.uniform(-0.5,0.5)

###########################################################
def f_0(t):
    return math.sin(1*w*t)+math.sin(2*w*t)+math.sin(3*w*t)

###########################################################
def f(t):
    return f_0(t)+d
####################################################################
def gauss(t):
    return (1/(sig*math.sqrt(2*math.pi)))*math.exp(-t**2/(2*sig**2))

#####################################################################
f0=[]
f1=[]
g1=[]
g2=[]
t=0
for i in range(2*N):
    if t<t_max:    
        f0.append(f_0(t))
        f1.append(f(t))
        g1.append(gauss(t))
        g2.append(gauss(t))
        t+=dt

f1_fft=fft(f1)
g1_fft=fft(g1)
g2_fft=ifft(g2)
f1=(f1_fft*(g1_fft+g2_fft))
print(f1)
f_max=max([abs(i) for i in f1])
print(f_max)
#####################################################
