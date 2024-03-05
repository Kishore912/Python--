x={1,2,3,4}
print(x)

#----------------------------------------------------------

y={1,2,3,4}
print(type(y))
print(len(y))

#----------------------------------------------------------

q=set((1,2,3,4)) #set constructor
print(q)

#-----------------------------------------------------------

p={1,2,3,4}
s={5,6,7,8}
p.update(s)
print(p)

#--------------------------

k = p.union(s)
print(k)

#------------------------------------

n={1,"apple",True,3}
n.add(46)
print(n)
n.pop()
print(n)
n.remove("apple")
print(n)
n.clear()
print(n)

#---------------------------------------------------

a={"ram" , "sita" , "gopal" , "jim"}
for x in a:
    print(x)

#for i in range(len(a)):
 #   print(a[i])     #cant use this method