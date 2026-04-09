import random

while True:
    user_action = input("Enter a choice(rock,paper,scissors): ")
    possible_actions = ["rock","paper","scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou choose {user_action}, computer choose {computer_action}.\n")

    if user_action == computer_action:
        print("Its a tie.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You win. Paper covers rock.")
        else:
            print("You lose. Scissors cuts paper.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You win. Scissors cuts paper.")
        else:
            print("You lose. Rock smashes scissors." )
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You win. Rock smashes scissors.")
        else:
            print("You lose. Paper covers rock")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again != "y":
        break
    