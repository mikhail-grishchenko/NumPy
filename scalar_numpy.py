import numpy as np
import random

def numpy_scalar(a, b):
  result = np.dot(a,b)
  return result

a = np.random.randn(3,)
b = np.random.randn(3,)

print(a)
print(b)
print(numpy_scalar(a,b))

%timeit()