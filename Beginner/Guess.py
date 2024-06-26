
secret_number = 6
guess_count = 0
guess_limit = 3
out_of_guesses = False
guess = 0

while not out_of_guesses:
    guess_count += 1
    guess = int(input("Enter a guess:"))

    if guess_count != guess_limit:
        pass
    else:
        out_of_guesses = True
    if guess == secret_number:
        break
if out_of_guesses == True and guess != secret_number:
    print("You are out of guesses, try again next time")
if guess == secret_number:
    print("Congratulations, You won the game")
