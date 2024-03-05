list1=["apple" , "orange" , "pinapple"]
list2=[1 , 2 , 3 , 4]
list3=[True , False , True]
list4=["apple" , 23 , True , "GT"]
print(list1)
print(list2)
print(list3)
print(list4)
print(len(list4))
print(type(list3))

#-------------------------------------------
list5=list(("r34" , "r33" , "r32"))
print(list5)
#-------------------------------------------
print(list4[1:4])
#-------------------------------------------
if True in list3:
    print("o yeah")
else:
    print("no ")    

#-------------------------------------------

list6=[1,2,3,4,5,6]
list6[2]=9
print(*list6) # using * symbol we can print with out list
list6[1:3]=11,12
print(list6)
list6[1:6]=43,23   # from 1 to 6 all the values will be 43,23 other values will move accordindly
print(list6)

#insert()

list7=[12,23,34,56,67,89]
list7.insert(2,65)
print(list7)

#-----------------------------------------------------------
# you can also create a list using a range and print statement

print(list(range(100)))
