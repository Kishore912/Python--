kid=["priya" , "ram" , "arun"]
kid.sort()
print(kid)

#--------------------------------------------------------------------------

country = ["india" ,"china" , "pakistan"]
country.sort(reverse=True)
print(country)

#---------------------------------------------------------------------------

def gat(e):
    return len(e)
dish=["biriyani" , "jagery" , "tamily"]
dish.sort(key=gat)
print(dish)

#-----------------------------------------------------------------------------

def kishore(e):
    return e["age"]
person=[{'name':'kishore','age':41}    , {"name":"preethi" , "age":22} , {"name":"hemanth" , "age":32 }]
person.sort(key=kishore)
print(person)

#---------------------------------------------------------------------------------------------------------------------------