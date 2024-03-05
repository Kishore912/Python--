from art import logo,vs
from game_data import data
import random
import os

def format_data(account):
    # format the account data into a printable format
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr},from {account_country}"

def check_answer(guess,a_follower,b_follower ):
    #Take the user guess and follower account and return if they got it right.
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

# display the art
print(logo)
score=0
game_should_continue = True
account_b = random.choice(data)
#Make the gsme repeatable
while game_should_continue:
    #generate a random account from the game_data
    #making account at poisition B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Against B:{format_data(account_b)}.")    

    # ask users for a guess
    guess=input("Who has more followers Type 'A' or 'B' ").lower()

    #check is user is correct
    # get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    os.system("cls")
    #Give user feedback on their guess
    #score keeping
    if is_correct:
        score+=1
        print(f"you are right. current score {score}")
    else:
        game_should_continue = False
        print(f"Sorry that's wrong . final score {score}")    