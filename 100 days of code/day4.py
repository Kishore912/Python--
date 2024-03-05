import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇 
user=int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. "))

if user==0:
  print(rock)
elif user==1:
  print(paper)
elif user==2:
  print(scissors)
else:
  print("you entered a invalid number , you lose!") 
  
computer=[rock,paper,scissors]
random_computer=random.choice(computer)
print("computer:",random_computer)
if(user==0) and (random_computer==rock):
  print("Draw")
elif(user==1) and (random_computer==paper):
  print("Draw")  
elif(user==2) and (random_computer==scissors):
  print("Draw")
elif(user==0) and (random_computer==paper):
  print("you lose")
elif(user==0) and (random_computer==scissors):
  print("you win")
elif(user==1) and (random_computer==rock):
  print("you win") 
elif(user==1) and (random_computer==scissors):
  print("you lose")
elif(user==2) and (random_computer==rock):
  print("you lose")
elif(user==2) and (random_computer==paper):
  print("you win")  
