class Kishore:
    def __init__(self,name,age):
        self.a=name
        self.b=age
    def My_func(x):
        return f"My name is {x.a} and iam {x.b}"
    def __str__(self):
        return f"my age is {self.b}"
object1=Kishore("kishore",21) 
print(object1.My_func())       
print(object1)

object1.b =22
print(object1)