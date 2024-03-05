def kishore():
    print("hi")
kishore()    

#-----------------------------------------

def preethi(x):
    return 10*x
print(preethi(2))    

#-----------------------------------------

def void(name):
    print(name + " is a bad boy")
void("kishore")   

#------------------------------------------

def luna(*description):        #if u dont know how many arguments will be passed then add astreik
    print("her age is : " , description[0])
    print("her blood group is : " + description[1])
    print("her weight is : " , description[2])
luna(21 , "O+ve" , 67)

#----------------------------------------------------------------

def children(child1 , child2 , child3):
    print(child2)
children(child1="kishore",child2="preethi" ,child3="kutty")

#----------------------------------------------------------------

def gop(**age):          #if u dont know how many keywords will be add then add double astreik
    print("age of kishore is : " , age["kishore"])
    print("age of preethi is : " , age["preethi"])
gop(kishore=12 , preethi=21)

#-----------------------------------------------------------------

def country(state="kerala"):
    print("i love " + state)
country()
country("TamilNadu")
country("Mumbai")    

#------------------------------------------------------------------------

def Auto(Mobiles):
    for x in Mobiles:
        print(x ,end=" ")
        if x=="tesla":
           break
cars=["GT" , "lamborgini" , "tesla" , "minicooper"]
Auto(cars)    

#-----------------------------------------------------------------------

