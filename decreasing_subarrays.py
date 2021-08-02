import numpy as np
def split_decreasing(x):
    # Check if following value is greater
    ix = np.less(a[:-1], a[1:])
    # Use the indices where the above is True
    # to split the array
    return np.split(a, np.flatnonzero(ix)+1)
 
a = np.random.randint(1,20,20)
print ("Original array:",a)
# array([12, 15,  3,  7, 18, 18,  9, 16, 15, 19])
print("Split array:")
print(split_decreasing(a))