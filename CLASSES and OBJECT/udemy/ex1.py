#class is a blue print

# class Kishore:                      # first letter should be in capital
#     pass
# user1 = Kishore()      
# user1.id="001"
# user1.name = "kishore"
# print(user1.name)
# print(user1.id)

# user2 = Kishore()
# user2.id = "002"
# user2.name = "Nandha"
# print(user2.id)
# print(user2.name)

# attributes are the things that the objects will have
# Methods are the things that the object does
# to overcome the above repeatation of the code we are going to initialize the constructor

class Kishore:   
    def __init__(self):
        print("initializing.....")   # this constructor get called when ever a new object is created
user1 = Kishore()      
user1.id="001"
user1.name = "kishore"
print(user1.name)
print(user1.id)

user2 = Kishore()
user2.id = "002"
user2.name = "Nandha"
print(user2.id)
print(user2.name)