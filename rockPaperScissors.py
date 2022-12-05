import random
actions = ["rock", "paper", "scissors"]
user = input("Enter a choice (rock, paper, scissors): ")
computer = random.choice(actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}.")
elif user == "rock":
    if computer == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user == "paper":
    if computer == "rock":
        print(" You win!")
    else:
        print(" You lose.")
elif user == "scissors":
    if computer == "paper":
        print(" You win!")
    else:
        print("You lose.")
