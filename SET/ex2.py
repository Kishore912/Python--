x={1,2,3,4}
y={1,2,5,6}
x.intersection_update(y)
print(x)

#-------------------------------------------------

a={1,2,3,4}
b={1,2,5,6}
c=a.intersection(b)
print(c)

#-------------------------------------------------

z={1,2,3,4}
v={1,2,5,6}
z.symmetric_difference_update(v)
print(z)

#----------------------------------------------------

o={1,2,3,4}
p={1,2,5,6}
j=o.symmetric_difference(p)
print(j)

#------------------------------------------------------

l={1,2,3,4}
k={1,2,5,6}
l.difference_update(k)
print(l)
m=l.difference(k)
print(m)

#-------------------------------------------------------

A={2,3,4,5}
B={2,3,7,8}
C=A.isdisjoint(B)
print(C)
S=A.issubset(B)
print(S)
D=A.issuperset(B)
print(D)
#------------------------------------------------------

