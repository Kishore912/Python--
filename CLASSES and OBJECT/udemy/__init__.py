class Car:
    def __init__(self,Gear,Tiers):
        self.Gear = Gear
        self.Tiers = Tiers
        self.Transmission = "v12"
car1 = Car(6,4)      # here u dont need to create a attributes like u created in ex1.py instead u can just initialize them and call it when ever u needed
print(car1.Gear)
print(car1.Transmission)        # we dont need to pass the attribute for transmission beacuse the value of it is given default we can just use the default value by calling it

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("_________________________________________________________________________________")

class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.following = 0  #for user1 = 1
        self.followers = 0  #for user2 = 1
    def follow(self,user):
        user.followers+=1
        self.following+=1
user1 = User(1,"kishore") 
user2 = User(2,"Nandha")
user1.follow(user2)            
print(user1.followers)
print(user1.following)       
print(user2.followers)
print(user2.following) 

# in line 24 first the user1 object calls the follow fuction and passing user2 object as a attribute
# now it increments the user2.followers to 1 in constructor and user1.following to 1 in constructor
# when u try to print line 25 it goes to constructor where user1.followers is equal to 0
# same as the following