import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number from 0 to 9 and you have to guess the number to win the game, one digit at a time.")
print("The game ends when you get 1 hero!")

while playing:
    guess = input("Give me a good guess \n")
    if number == guess:
        print("You win.")
        print("The number was", number)
        break

    else:
        print("Your guess is not right, try again, \n")
