import numpy as np
arr1=np.round(10*np.random.rand(3,3))
arr2=np.round(10*np.random.rand(3,3))

print(arr1)
print(" ")
print(arr2)
print(" ")

new_arr1 = np.concatenate((arr1,arr2))
print(new_arr1)
print(" ")

new_arr2 = np.concatenate((arr1,arr2) , axis=1)
print(new_arr2)
print(" ")

X=np.hstack((arr1,arr2))
Y=np.vstack((arr1,arr2))
Z=np.dstack((arr1,arr2))
print(X)
print(" ")
print(Y)
print(" ")
print(Z)

