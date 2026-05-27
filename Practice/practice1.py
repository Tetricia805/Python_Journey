# guess game

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess_number = int(input("Enter the guess number of your choice:"))

    if guess_number == secret_number:
        print("Congrats 🎉👏 you have passed")
        break

    elif guess_count < guess_limit:
        # give hints if they have remaining guesses
        if guess_number > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

    else:
        print("Try again")

    guess_count += 1
else:
    print(f"Sorry You have failed, Out of guesses. The correct number was {secret_number}")


# Classes: They are used to define new types