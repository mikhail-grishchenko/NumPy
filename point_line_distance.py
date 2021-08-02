import numpy as np
def distance(X, Y, p):
    T = Y - X
    L = (T**2).sum(axis=1)
    U = -((X[:,0] - p[...,0]) * T[:,0] + (X[:,1] - p[...,1]) * T[:,1]) / L
    U = U.reshape(len(U),1)
    D = X + U * T - p
    return np.sqrt((D**2).sum(axis=1))
    
X = np.random.uniform(-10,10,(10,2))
Y = np.random.uniform(-10,10,(10,2))
p  = np.random.uniform(-10,10,( 1,2))
print (X,"\n")
print (Y,"\n")
print (p,"\n")
print(distance(X, Y, p))