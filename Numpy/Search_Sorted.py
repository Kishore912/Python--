import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(np.searchsorted(arr,5))
print(np.searchsorted(arr,5,side='right'))

#------------------------------------

print(np.searchsorted(arr,[10,11,12]))

#searchsorted will performa binary tree search in the array
