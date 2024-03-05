dict1 = {'name' : 'kishore' , 'age' : 20 , 'hobbie' : 'cricket'}
print(dict1)
dict1['height'] = 54
print(dict1)
print(dict1['height'])
print(dict1.get("age"))

#----------------------------------------------------------------------------

dict2 = dict(name="preethi" , age = 25 , height = 34 ) #constructor 
print(dict2)


#--------------------------------------------------------------

print(len(dict1))
print(len(dict2))
print(type(dict1))
print(type(dict2))

#------------------------------------------------------------------------

print(dict1.keys())
print(dict2.keys())
print(dict1.values())
print(dict2.values())
print(dict1.items())
print(dict2.items())

#--------------------------------------------------------------------------
