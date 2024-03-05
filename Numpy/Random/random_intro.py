from numpy import random
x=random.randint(50)
y=random.randint(50,size=(3,3))
print(x)
print(y)

#-------------------------------------------

z=random.rand()
print(z)
v=random.rand(2,3)
print(v)

#--------------------------------------------

d=random.choice([1,2,3,4])
print(d)
c=random.choice([1,2,3,4],size=(3,3))
print(c)