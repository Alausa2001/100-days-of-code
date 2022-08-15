#!/usr/bin/python3
import random
import rock_paper_scissors

choice = [rock_paper_scissors.rock, rock_paper_scissors.paper, rock_paper_scissors.scissors]

player_choice = int(input("Enter 0 for rock, 1 for paper or 2 for scissors: "))

random.seed()
computer_choice = random.randint(0, len(choice) - 1)
#if player_choice:
 #   print("Shine your eyes, didn't you see the instructions??")
#else:
 ##  print(f"Computer chose\n{choice[computer_choice]}\n")
if player_choice < 3:
    print(f"You chose\n{choice[player_choice]}\n")
    print(f"Computer chose\n{choice[computer_choice]}\n")
    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == 0 and computer_choice == player_choice + 1:
        print("You lose")
    elif player_choice == 0 and computer_choice == player_choice + 2:
        print("You win")
    elif computer_choice == 0 and player_choice == computer_choice + 1:
        print("You win")
    elif computer_choice == 0 and player_choice == computer_choice + 2:
        print("You lose")
    elif player_choice > computer_choice:
        print("You win")
    else:
        print("You lose")
else:
    print("Shine your eyes, didn't you see the instructions??")
