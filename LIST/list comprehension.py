fruits = ["apple" , "orange" , "mango" , "kiwi"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#-------------------------------------------------
addlist = [x for x in fruits if "a" in x]
print(addlist)

#------------------------------------------------

list1 =[x for x in range(11)]
print(list1)

#------------------------------------------------

list2 = [x for x in range(10) if x%2==0]
print(list2)

#-------------------------------------------------

list3 = [x for x in fruits if x!="apple"]                # printing all the elements other than apple
print(list3)

#---------------------------------------------------

list4 = [x if x!="apple" else "orange" for x in fruits]            #replacing apple with orange
print(list4)

#----------------------------------------------------

lst = [x.upper() for x in fruits if "a" in x]
print(lst)