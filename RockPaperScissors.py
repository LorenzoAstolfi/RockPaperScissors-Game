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

num = random.randint(0, 2)
choice = int(input("What do you choose? (0 = rock, 1 = paper, 2 = scissors) "))
game = [rock, paper, scissors]

print(game[choice] + "\n\nComputer choose: \n" + game[num] + "\n")

if choice == num:
    print("You draw!")
elif choice == 0:
    if num == 1:
        print("You lose!")
    elif num == 2:
        print("You win!")
elif choice == 1:
    if num == 0:
        print("You win!")
    elif num == 2:
        print("You lose!")
elif choice == 2:
    if num == 0:
        print("You lose!")
    elif num == 1:
        print("You win!")
