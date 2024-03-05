import numpy as np
arr=np.array([1,2,3,4,5,6,7])
new_array = np.array_split(arr,3)
print(new_array)

#--------------------------------------

#arr1 =np.round(10*np.random.rand(3,3))
#print(arr1)
#new_array2=np.array_split(arr1,2)
#print(new_array2)

arr2 = np.array([[1,2,3,4],[5,6,7,8]])
new_array3 = np.array_split(arr2,2,axis=1)
print(new_array3)

 #hspit is similar to axis=1

arr3 = np.array([[1,2,3,4],[5,6,7,8]])
new_array4 = np.hsplit(arr3,2)
print(new_array4)