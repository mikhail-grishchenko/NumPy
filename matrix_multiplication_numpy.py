import numpy as np
from datetime import datetime
start_time = datetime.now()

a1 = np.random.randint(1, 3, size=(100, 100))
b1 = np.random.randint(1, 3, size=(100, 100))
print("array 1:\n",a1,"\n")
print("array 2:\n",b1,"\n")
print("array 3:\n",a1*b1,"\n")

end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
