def LN(N,A,i):
    L=[[1 if i==j else 0 for i in range(N)]for j in range(N)]
    for j in range(N):
        l=A[i][j]/A[i][i]
        l=round(l,3)
        if j<i:
            L[i][j]=l
    return L

####################################

def matmatmul(A,B,N):
    X=[[0 for j in range(N)]for i in range(N)]
    con=0
    for i in range(N):
        for j in range(N):
                for k in range(N):
                    con=con+A[j][i]*B[i][j]
                con=round(con,3)
                X[i][j]=con
    return X

####################################


def Lmatrix(N,A) :
    L=[[1 if i==j else 0 for i in range(N)]for j in range(N)]
    for i in range(N):
        for j in range(N):
            l=A[i][j]/A[i][i]
            l=round(l,3)
            if j<i:
                L[i][j]=l
    return L

####################################

def vmatmul(A,x):
    y=[0 for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            con=A[j][i]*x[i]
            con=round(con,3)
        y[i]=con
    return y

####################################

c=[3,0.7,2,0.6,3,1,]
x=[2,0.4,1,0.5,3,2,]

A1=[[x[i]**j for j in range(len(x))]for i in range(len(x))]

y=vmatmul(A1,c)
print(y)

L=Lmatrix(len(x),A1)
print(L)
L3=0
for i in range(len(x)):
    for i in range(len(x),-1):
        if i==0:
            L1=LN(len(x),A1,i)
            L2=LN(len(x),A1,i-1)
            # L3=matmatmul(L1,L2,len(x))




