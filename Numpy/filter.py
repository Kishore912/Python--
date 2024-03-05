import numpy as np
#method 1
a=np.array([1,2,3,4])
b=[True,False,True,False]
c=a[b]                             # filter out the values based on boolean value as an index
print(c)

#---------------------------------------------------------------------------------------------------------

X= []
for i in a:
    if i>2:
        X.append(True)                 #method 2
    else:
        X.append(False)  
Y=a[X]
print(Y)          

#------------------------------------------------------------------------------

filter=a%2==0
Z=a[filter]
print(Z)                             #method 3

#-------------------------------------------------------------------
