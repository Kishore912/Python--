import drawing
import os
print(drawing.art)

dice={}
x=False
while not x:
    name=input("What is your name? : ")
    bid=int(input("What is your bid? : $"))
    dice[name]=bid
    value=input("Are there any bidders Type 'YES' or 'NO' ")
    if value=="NO":
        x=True
    elif value=="YES":
        os.system('cls')
dice_key=list(dice.keys())
dice_value=list(dice.values())
max_value=max(dice_value)
position=dice_value.index(max_value)
highest_bidder=dice_key[position]
print(f"The winner is {highest_bidder} with a bid of ${max_value}")

