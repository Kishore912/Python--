#removing in a diictionary

dict1 = {'name' : 'kishore' , 'age' : 20 , 'hobbie' : 'cricket'}
dict1.pop("age")
print(dict1)
dict1.popitem()
print(dict1)

#----------------------------------------------------------------------

dict2 = {'name' : 'kishore' , 'age' : 20 , 'hobbie' : 'cricket'}
del dict2['name']
print(dict2)
dict2.clear()
print(dict2)
del dict2
print(dict2)
