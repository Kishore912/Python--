import random
from art import logo
print(logo)

print("Welcome to the number gussing game")
print("Iam thinking of a number between 1 and 100.")
number = random.randint(1,100)
Type_of_input = input("Choose a difficulty. Type 'easy' or 'hard' : ")
flag=True

def easy():    
    i = 10
    while i>0 :
        print(f"You have {i} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if guess > number:
            print("Too high\nGuess again.")
        elif guess < number:
            print("Too Low\nGuess again.")    
        else:
            print(f"You got it! The answer was {number} ")  
            global flag
            flag = False
        i-=1      



def hard():
    i = 5
    while i>0 :
        print(f"You have {i} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))
        if guess > number:
            print("Too high\nGuess again.")
        elif guess < number:
            print("Too Low\nGuess again.")    
        else:
            print(f"You got it! The answer was {number} ")  
            global flag
            flag = False
        i-=1      



if Type_of_input == "easy":
    easy()
else:
    hard()
    