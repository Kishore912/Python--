def kishore():
    print("hi")
kishore()    

#---------------------------------------------------

def gop(a):
    print("hi" , a)
gop("jp")

#--------------------------------------------------

def fall(x,y):
    print(x,"is very possessive on ",y)
fall("zara","hary")    

#---------------------------------------------------

def vap(*kid):
    print("hi this is my first child" ,kid[0])
vap("kio" , "charlie" , "haris")    

#-----------------------------------------------------

def bap(child1 , child2 , child3):
    print(child3)
bap(child1="kishore" , child2="jak" , child3="priya")

#----------------------------------------------------------------

def cas(**chef):
    print("hi" , chef["name"])
cas(name="kishore" , age="20" , color = "brown")    

#-------------------------------------------------------------

def joke(names):
    for i in names:
        print(i , end=" ")
child =["priya" , "amala" , "bob"]
joke(child)         
