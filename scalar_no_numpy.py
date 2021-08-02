import random

def no_numpy_scalar(a2, b2):
    result = 0
    for i, j in zip(a2, b2):
        result += i*j
    return result

a2  = []
for i in range(3):
  a2.append(random.uniform(-100,100))
b2 = []
for i2 in range(3):
  b2.append(random.uniform(-100,100))

print(a2)
print(b2)
print(no_numpy_scalar(a2,b2))
%timeit()