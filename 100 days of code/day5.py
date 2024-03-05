#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password=""
#for i in range(1,nr_letters+1):
  #a=random.choice(letters)
  #password+=a

#for x in range(1,nr_symbols+1):
  #b=random.choice(symbols)
  #password+=b

#for z in range(1,nr_numbers+1):
  #c=random.choice(numbers)
  #password+=c
#print(password)
  



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list=[]                   #first we creating the empty list to add the stuffs
for i in range(1,nr_letters+1):    #using for loop from the range of 1 to 4
  a=random.choice(letters)         #then randomize the letters for each range  
  password_list+=a                 #then add those letters in the previously created list

for x in range(1,nr_symbols+1):    #same for the symbol
  b=random.choice(symbols)         #followed by the letters , the symbols are added to the list
  password_list+=b

for z in range(1,nr_numbers+1):     #same for the numbers
  c=random.choice(numbers)
  password_list+=c

  #so finally we have all the random stuffs in the list but it is in the order like letters followed by symbols followed by numbers
  #to change that order we have used the random.shuffle()
  
random.shuffle(password_list)      
password=""
for i in password_list:   #and finaly the order of random stuffs are changedand we loop through the list to get the stuffs  
  password+=i             #and add it in the password to print it
print(password)  
  
  
  
