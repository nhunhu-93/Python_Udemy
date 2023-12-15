# Trò chơi kéo búa bao
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

choice = [rock, paper, scissors]
choice_person = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors: "))

if choice_person >=3 and choice_person <0:
    print("You type an invalid, you lose")
else:
    print(choice[choice_person])

    print("Computer chose")
    random_computer = random.choice(choice)
    print(random_computer)

    if choice_person == 0:
        if random_computer == choice[2]:
            print("You win")
        elif random_computer == choice[0]:
            print("Draw")
        else:
            print("You lose")
    elif choice_person == 1:
        if random_computer == choice[2]:
            print("You lose")
        elif random_computer == choice[0]:
            print("You win")
        else:
            print("Draw")
    else :
        if random_computer == choice[2]:
            print("Draw")
        elif random_computer == choice[0]:
            print("You lose")
        else:
            print("You win")