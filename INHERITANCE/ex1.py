class Kishore:
    def __init__(self,fname,lname):
        self.x=fname
        self.y=lname
    def display(self):
        print(self.x,self.y)
class Student(Kishore):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.z=14
        self.s=year
b=Student("jani", "kuily",2020)
b.display()
print(b.z)                  
print(b.s)

#-------------------------------------------------------------------

