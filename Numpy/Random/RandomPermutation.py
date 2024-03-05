from numpy import random
import numpy as np
arr=np.array([1,2,3,4])
random.shuffle(arr)
#------or-----------
# random.permutation(arr)
print(arr)