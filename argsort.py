import numpy as np
np.random.seed(22)
a = np.random.randint(0, 10, (5, 3))
print(a)
print (a[a[:,0].argsort()])