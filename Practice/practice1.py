# guess game

secret_number = 7
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess_number = int(input("Enter the guess number of your choice:"))

    if guess_number == secret_number:
        print("you have passed")
        break

    else:
        print("try again")

    guess_count += 1
else:
    print("Sorry You have failed, Out of guesses")
