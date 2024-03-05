x="hello"                        #str
print(x)
print(type(x))


y=12                             #int
print(y)
print(type(y))


z=12.2                           #float
print(z)
print(type(z))


s=1j                             #complex
print(s)
print(type(s))


d=["apple","orange","banana"]     #list
print(d)
print(type(d))


e=("apple","orange","banana")     #tuple
print(e)
print(type(e))


f={"apple","orange","banana"}     #set
print(f)
print(type(f))


h={"name":"kishore" , "age":"20"}  #dict
print(h)
print(type(h))


j=frozenset({"apple","orange","banana"})    #frozenset
print(j)
print(type(j))


k=range(10)           #range
print(k)
print(type(k))


l=True                #bool
print(type(l))


AS=None                #NoneType
print(type(AS))


m = b"Hello"           #bytes
print(m)
print(type(m)) 


a=bytearray(4)         #bytearray
print(a)
print(type(a))


b=memoryview(bytes(4))  #memoryview
print(b)
print(type(b))


A=dict(name="kishore" , age="20")              #typecasting dict or specifying datatype
print(A)


B=list(("apple","orange"))                      #typecasting dict or specifying datatype of list , tuple , dict  , set , frozenset
C=tuple(("apple" , "orange"))
D=set(("apple" , "orange"))
E=frozenset(("apple" , "orange"))
print(D)
print(E)
print(B)
print(C)


import random
W=random.randrange(1,10)            #import random module to print a ramdom number btw 1 and 10
print(W)