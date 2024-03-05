t1 = ("scoda" , "mustang" , "civic")
t2 = list(t1)            #converts the tuple into list
t2.append("skyline")     #adding value
t1 = tuple(t2)           #converts list into tuple 
print(t1)           

#-------------------------------------------------------------------

#unpacking of a tuple

tuple1 = ("python" , "java" , "R" , "sql")
(easy , complex , morecomplex , queries) = tuple1
print(easy)
print(complex)
print(morecomplex)
print(queries)

#--------------------------------------------------------------------

tuple2 = (1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9)
(one , two , three , *four , five ) = tuple2       #when no of variable is less than the no of values then we can use the Astreik symbol
print(one)                                         
print(two)
print(three)
print(four)
print(five)

#--------------------------------------------------------------------

#LOOPING IN TUPLE

x=("india" , "china" , "bangladesh" , "australia")
for i in x:
    print(i)       

#---------------------------------------------------------------

for i in range(len(x)):
    print(x[i])

#------------------------------------------------------------------

y=0
while y<len(x):
    print(x[y])
    y+=1    