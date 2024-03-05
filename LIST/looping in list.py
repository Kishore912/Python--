cars=["carens" , "seltos" , "carnival"]  #looping using elements;
for x in cars:
    print(x)

#------------------------------------------------------

for i in range(len(cars)):
    print(cars[i])                  #looping using the index in for loop;
     
#-------------------------------------------------------

j=0
while j<len(cars):
    print(cars[j])         #looping using index in while loop;
    j+=1  

#----------------------------------------------------------

[print(j) for j in cars]       #looping using list comprehension;