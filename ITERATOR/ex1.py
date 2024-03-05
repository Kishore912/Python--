tuple1=("apple", "orange" , "blueberry" , "kiwi")
x=iter(tuple1)
print(next(x))
print(next(x))
print(next(x))
print(next(x))

#--------------------------------------------------------

myFavoriteCar = "Volkswagen"
y=iter(myFavoriteCar)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

#--------------------------------------------------------

class Messi:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        d=self.a
        self.a+=2
        return d    
v=Messi()
zz=iter(v)
print(next(zz))        
print(next(zz))
print(next(zz))
print(next(zz))
print(next(zz))


#-------------------------------------------------------------


class preethi:
    def __iter__(self):
        self.e=1
        return self
    def __next__(self):
        if self.e<=50:    
           m=self.e
           self.e+=5
           return m
        else:
            raise StopIteration
bb=preethi()
jop=iter(bb)
for x in jop:
    print(x)            