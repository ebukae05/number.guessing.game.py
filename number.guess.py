import random

print("hey, welcome to my game")

def random_numb():
    random_int = random.randint(1,100)
    return random_int

def diff_level():
    diffLev = int(input("what difficulty: 1 = easy, 2 = medium, 3 = hard: "))
    if diffLev == 1:
        return 10
    elif diffLev == 2:
        return 5
    elif diffLev == 3:
        return 3
    else:
        print("ERROR")
        return None

guess = diff_level()

if guess is not None:
    print(f"you have {guess} guesses")
else:
    print("not a valid number, try again later.")


def user_guess(guess):
    secretNumb = random_numb()
    absoluteGuess = 0

    while guess > 0:
        try:
            userGuess = int(input(f"You have {guess} guesses left. Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        absoluteGuess += 1
        if userGuess == secretNumb:

            return f"YAY, YOU WON IN {absoluteGuess} ATTEMPTS!"
        elif userGuess > secretNumb:
            guess -= 1
            print(f"TOO HIGH, {guess} GUESSES LEFT.")
        elif userGuess < secretNumb:
            guess -= 1
            print(f"TOO LOW, {guess} GUESSES LEFT.")
    else:
        return "GAME OVER"

game = user_guess(guess)
print(game)
