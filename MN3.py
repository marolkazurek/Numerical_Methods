import math
###################################################################
def vsub(x,y):                                                    # 
    z=[x[i]-y[i] for i in range(len(x))]                          #
    return z                                                      #
###################################################################
def vadd(x,y):                                                    #
    z=[x[i]+y[i] for i in range(len(x))]                          #
    return z                                                      #
###################################################################
def vadiv(x,y):                                                   #   
    z=[round(x[i]/y[i],3) for i in range(len(x))]                 #
    return z                                                      #
###################################################################
def vecmult(x,y):
    z=[0 for i in range(len(x))]
    con=0
    for i in range(N):
        for j in range(N):
            con=con+x[j][i]*y[i][j]
        con=round(con,3)
        z[i][j]=con
    return z

###################################################################
def transp(A):
    B=[[A[j][i] for i in range(len(A))] for j in range(len(A))]
    return B
#########################################################################
def MNS(b,A,x):                                                         #
    r_k=vsub(b,vmatmul(A,x))                                            #
    a=vecmult(transp(r_k),r_k)/(vecmult(transp(r_k),vmatmul(A,r_k)))    #
    x=vadd(x,a*r_k)                                                     #
    R_K=math.sqrt(transp(r_k)*r_k)                                      #
    while  R_K > 10**(-6):                                              #
        r_k=vsub(b,vmatmul(A,x))                                        #
        a=vecmult(transp(r_k),r_k)/(vecmult(transp(r_k),vmatmul(A,r_k)))#
        x=vadd(x,a*r_k)                                                 # 
    return x                                                            #
                                                                        #
#########################################################################
def vmatmul(A,x):                                                  #
    y=[0 for i in range(len(A))]                                   #
    for i in range(len(A)):                                        #
        for j in range(len(A)):                                    #
            con=A[j][i]*x[i]                                       #
            con=round(con,3)                                       #
        y[i]=con                                                   #
    return y                                                       #
####################################################################
N=10
m=5

A=[[1/(1+abs(i-j)) if (abs(i-j)<=m) else 0 for j in range(N)]for i in range(N)]


b=[i for i in range(N)]

x1=[0 for i in range(N)]

x1=MNS(b,A,x1)

print('VECTOR X1:\n',x1)

x2=[1 for i in range(N)]

x2=MNS(b,A,x2)

print('VECTOR X2:\n',x2)




#Wektor wlasny diagonalizacja 