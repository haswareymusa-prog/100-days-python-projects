import random

users_draw = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: ")
choices = ["Rock", "Paper", "Scissors"]
computer_draws = random.choice(choices)

if users_draw == "0":
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
if users_draw == "1":
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
if users_draw == "2":
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

print("Computer chose:", computer_draws)

if computer_draws == choices[0]:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
if computer_draws == choices[1]:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
if computer_draws == choices[2]:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

if users_draw == "0":
    if computer_draws == choices[1]:
        print("You Lose.")
    if computer_draws == choices[2]:
        print("You Win!")
    if computer_draws == choices[0]:
        print("Draw.")
if users_draw == "1":
    if computer_draws == choices[2]:
        print("You Lose.")
    if computer_draws == choices[0]:
        print("You Win!")
    if computer_draws == choices[1]:
        print("Draw.")
if users_draw == "2":
    if computer_draws == choices[0]:
        print("You Lose.")
    if computer_draws == choices[1]:
        print("You Win!")
    if computer_draws == choices[2]:
        print("Draw.")















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
