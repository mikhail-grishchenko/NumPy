import numpy as np
Z = np.arange(10000)
np.random.shuffle(Z)
n = 5
print (Z[np.argpartition(-Z,n)[:n]])