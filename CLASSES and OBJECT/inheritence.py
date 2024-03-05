class Kishore:
    def __init__(self,name,age):
        self.a=name
        self.b=age
    def My_func(abc):
        print(f"My name is {abc.a} and {abc.b} years old")

class Child(Kishore):
    def __init__(self, name, age,height):
        super().__init__(name, age)
        self.height = height
object1 = Child("kishore",21,"5'8")
print(object1.height)
object1.My_func()        