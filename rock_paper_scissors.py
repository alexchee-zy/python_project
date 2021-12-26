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


import random
rpc = [rock, paper, scissors]


# my choice
choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
your_choice = rpc[choice]


# npc choice
npc = random.randint(0,2)
npc_choice = rpc[npc]

print("npc_choice:\n" + npc_choice)
print("your_choice:\n" + your_choice)

# Compare the choice between npc and yours
if your_choice == rock and npc_choice == scissors:
    print("You win!")
elif your_choice == scissors and npc_choice == paper:
    print("You win!")
elif your_choice == paper and npc_choice == rock:
    print("You win!")
elif your_choice == npc_choice:
    print("It's a Draw")
else:
    print("You lose!")