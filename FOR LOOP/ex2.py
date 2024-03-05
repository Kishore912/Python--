q=["apple" , "orsnge" , "banana" , "papaya"]   
for x in q:
    if x=="banana":
        continue
    print(x)

# NESTED FOR LOOP

lst1=[1]
lst2=[1,2,3,4,5,6,7,8,9,10] 
for x in lst1:
    for y in lst2:
        print(x  , "*" , y , "=", x*y )   