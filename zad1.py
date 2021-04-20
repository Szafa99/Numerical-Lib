import numpy as np     

L=np.array([(1,0,0,0),(-1,1,0,0),(2,-1,1,0),(-3,2,-2,1)])
U=np.array([(2,1,-1,3),(0,1,-1,3),(0,0,-1,3),(0,0,0,3)])
b=np.array([(12,-8,21,-26)])

def forward_subs(L,b):
    y=[]
    for i in range(len(b)):
        y.append(b[i])
        for j in range(i):
            y[i]=y[i]-(L[i,j]*y[j])
        y[i]=y[i]/L[i,i]

    return y

def back_subs(U,y):
    x=np.zeros_like(y)
    for i in range(len(x),0,-1):
      x[i-1]=(y[i-1]-np.dot(U[i-1,i:],x[i:]))/U[i-1,i-1]

    return x

def solve_system_LU(L,U,b):
    y=forward_subs(L,b)
    x=back_subs(U,y)

    return x

print(solve_system_LU(L,U,b))