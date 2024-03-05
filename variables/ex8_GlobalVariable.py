def hello():                      # create a method with a local variable and print it by call the method name  
    x="helo man"
    print(x)
hello()                   


A= "summer"                        
def func1():                         # create a global variable and a method with a local variable and print the local 
    A="winter"                        #variable by calling the method and try to print the global variable outside
    print(A)                          #method 
func1()                            
print(A)    

 
P="audi"
def func2():
    global P              # we can also use "global " keyword to declare local variable as global variable
    P="car"               # same variable names are used here the new one will overwrite the old one 
    print(P)
func2()
print(P)    


T="iam a "
def func3():
    global V
    V="DataScientist"
    print(T,V)
func3()    