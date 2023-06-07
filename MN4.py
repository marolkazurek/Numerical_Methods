import math
###################################################################                                               #
def bi_method(A,acc):
    N=len(A)
    delta=[0 for i in range(N)]
    gamma=[0 for i in range(N)]
    for j in range(N):
        for i in range(N):
            delta[i]=A[i][j]
            gamma[i]=A[i][j-1]
    b=gamma[0]+delta[0]
    lp=-b
    pp=b
    x=(lp+pp)/2
    lzz=0
    wp=0
    wn=1
    for j in range(acc):
        for i in range(N):
            w=((delta[i]-j)*wn-(gamma[i]**2)*wp)
            wp=wn
            wn=w
            if is_sign_change(wp,wn):
                lzz+=1
        if lzz>1:
            pp=(lp+pp)/2
        else:
            lp=(lp+pp)/2
        x=(pp+lp)/2
        lzz=0
    print(x)
###################################################################
def is_sign_change(a,b):
    if a*b>0:
        return False
    else: return True



N=50
L=10
d_x=(2*L)/N
x_i=[-L+i*d_x for i in range(N)]
A=[[0 for i in range(N)]for j in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            A[i][j]=(d_x**(-2)+(x_i[i]**2)/2)
        if i==(j-1) or (i-1)==j:
            A[i][j]=-1/(2*d_x)**2


bi_method(A,100)




#transformacja hotellinga