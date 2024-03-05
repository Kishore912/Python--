#Looping in dictionary

dict1 = {'name' : 'kishore' , 'age' : 20 , 'hobbie' : 'cricket'}
for x in dict1:
    print(x)
for x in dict1.keys():   #to get a key using loop we can use either methods
    print(x)

#-------------------------------------------------------------------------------

dict2 = {'cars' : 'skyline' , 'color'  : 'blue' , 'topspeed' : '300kph'}
for x in dict2:
    print(dict2[x])
for x in dict2.values(): #to get a values we can use either methods
    print(x)


#--------------------------------------------------------------------------------

for x,y in dict2.items():  #to get a items in the dictionary use this method 
    print(x,y)

#----------------------------------------------------------------------------