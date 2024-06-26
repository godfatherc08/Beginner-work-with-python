import random
name = input("Please enter your name:")

print("Hello " + name + ", your secret number is between 1 and 20. "
             "Guess the number to obtain free credits. Good luck")

secret_number = random.randint(1, 20)
guess_count = 0
guess_limit = 3
guess = ""
out_of_guesses = False

while not out_of_guesses:

    guess_count += 1
    guess = int(input("Enter a guess:"))
    if guess_count != guess_limit:
        pass
    else:
        out_of_guesses = True
    if guess == secret_number:
        break
    elif guess not in range(1, 20):
        print("Guess is out of range, please try again")
    elif guess > secret_number:
        print("Try again with a lower number")
    else:
        print("Try again with a higher number")


if out_of_guesses == True:
    print("You are out of guesses, you lose")
    print("This was your secret number: " + str(secret_number))

if guess == secret_number:
    print("Congratulations, You have won the game.")
