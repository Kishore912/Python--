x = ["apple" , "banana" , "orange" , "mango" , "kiwi"]
x.sort()          # using sort() method we can sort in ascending order
print(x)

#---------------------------------------------------------------------

x.sort(reverse=True)
print(x)         # using reverse=True we can sort in descending order

#--------------------------------------------------------------------

y = [12 , 23 , 45 , 56 , 67 , 2 , 3]
y.sort()
print(y)
y.sort(reverse=True)
print(y) 

#-----------------------------------------------------------------------

x1 = ["apple" , "banana" , "orange" , "mango" , "kiwi"]
x1.reverse()
print(x1)                                            #using reverse()method we can print the last to first
y1 = [12 , 23 , 45 , 56 , 67 , 2 , 3]
y1.reverse()
print(y1)

#-----------------------------------------------------------------------

z= ["apple" , "banana" , "Orange" , "Mango" , "kiwi"]
z.sort()         #sort() is case sensitive first it will sort the uppercase and then comes to lower case
print(z)

#------------------------------------------------------------------------

v= ["apple" , "banana" , "Orange" , "Mango" , "kiwi"]
v.sort(key=str.lower)     #using key=str.lower both the upper case and lower case are sorted equally in ascending order
print(v)

#----------------------------------------------------------------------------------------------------