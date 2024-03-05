import numpy as np
arr=np.array([1,2,3,4,3,6,7,3])
result=np.where(arr == 3)
print(result)

#---------------------------------------

arr1=np.array([1,2,3,4,3,6,7,3])
even=np.where(arr1%2==0)
print(even)

#----------------------------------------

arr2=np.array([1,2,3,4,3,6,7,3])
odd=np.where(arr2%2!= 0)
print(odd)