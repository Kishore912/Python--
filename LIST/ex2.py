list1=[1,2,3,4]
list1.append(5)
print(list1)

#-------------------------------------------------------

list2=[1,2,3,4]
list3=[5,6,7,8]       #extend is used to join two list
list2.extend(list3)
print(list2)

#----------------------------------------------------------

list4=[1,2,3,4]
list5=(5,6,7,8)
list4.extend(list5)
print(list4)

#-------------------------------------------------------------

list6 = list2 + list3
print(list6)
#-------------------------------------------------------------

for x in list5:
    list4.append(x)  #joining two list
print(list4)    