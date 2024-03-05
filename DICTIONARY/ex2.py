#changing the items in the dictionary

dict1 = {'name' : 'kishore' , 'age' : 20 , 'hobbie' : 'cricket'}
dict1["name"]="preethi"    # change the value by either this method
print(dict1)
dict1.update({"age" : 25})    # or this method
print(dict1)


#adding the items in the dictionary

dict2 = {'cars' : 'skyline' , 'color'  : 'blue' , 'topspeed' : '300kph'}
print(dict2)
dict2['transmission']='manual'  #add by using this method 
print(dict2)
dict2.update({'owner':'paulwalker'})  #or by this method
print(dict2)


#