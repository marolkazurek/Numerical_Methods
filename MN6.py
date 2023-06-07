import cmath
######################################################
def b_element(k,a,z_j):
    if k==(len(a)-1):
        b_k=0
    elif k<(len(a)-1):
        b_k=a[k+1]+z_j+b_element(k+1,a,z_j)
    return b_k
######################################################
def complex_zero_finder(a,z_0,z_1):
    z_x=[]
    IT_MAX=20
    alpha=10**(-10)
    for l in range(len(a),0,-1):
        for j in range(1,IT_MAX):
            if j==1:
                z_j_1=z_0
                z_j=z_1
                Rj_1=a[0]+z_j_1*b_element(0,a,z_j_1)
                Rj=a[0]+z_j*b_element(0,a,z_j)
            z_j1=z_j-((Rj*(z_j-z_j_1))/(Rj-Rj_1))
            Rj1=a[0]+z_j1*b_element(0,a,z_j1)
            z_x.append(z_j)
            if abs(z_j1-z_j)<alpha:
                break
            z_j_1=z_j
            z_j=z_j1
            Rj_1=Rj
            Rj=Rj1
        a=[b_element(i,a,z_j) for i in range(l)]
    print(z_x)

# z_j1 == z_j+1
# Rj1  == R_j+1
# z_j_1== z_j-1
# Rj_1 == R_j-1
######################################################

#wspolczynniki
a=[]
a.append(complex(16,8))
a.append(complex(-20,14))
a.append(complex(4,-8))
a.append(complex(-4,1))
a.append(complex(1,0))
print(a)
###z####
z_0=complex(0,0)
z_1=complex(0.1,0.1)
###z####
complex_zero_finder(a,z_0,z_1)
