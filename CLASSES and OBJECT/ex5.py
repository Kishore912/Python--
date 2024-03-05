# NON PARAMETERIZED CONSTRUCTOR

class loop:
    def __init__(self):
        print("this is a non parametrized constructor")
    def func(self,name):
        print("hello "+name)
x=loop()
x.func("kishore")  


#PARAMETERIZED CONSTRUCTOR

class dope:
    def __init__(self,name):
        print("this is a parameterized constructor")
        self.a=name
    def google(self):
        print("hello " , self.a)
f=dope("kishore")        
f.google()