try:
    print(x)
except:
    print("x is not defined")    
else:
    print("the else part will not be executed ")
finally:
    print("the finally part will be executed")        

#-------------------------------------------------------------------------------

try:
    print("welcome")
    try:
        def display():
            d1={"name":"kishore" , "age":"20"}
            for x in d1:
                print(x)
        display()        
    except:
        print("failed at the second stage")
    else:
        print("else block for second stage")                
except:
    print("failed at the initial stage") 
else:
    print("else block for initial stage")
finally:
    print("finally the finally block got executed")               

#---------------------------------------------------------------------------------------------------------------------------


x=0
if x==0:
    raise Exception("x is equal to 0")