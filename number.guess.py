import random


def welcome_message():
    print("Welcome to the number guessing game!")


def get_number_range():
    numb1 = int(input("Please type a number: "))
    numb2 = int(input("Select another number: "))
    return numb1, numb2


def get_difficulty():
    difficulty = int(input("Select your difficulty (1=Easy, 2=Medium, 3=Hard): "))
    return difficulty


def get_random_number(numb1, numb2):
    return random.randint(numb1, numb2)


def play_game(numb1, numb2, random_integer, difficulty):
    if difficulty == 1:
        max_attempts = 10
    elif difficulty == 2:
        max_attempts = 5
    elif difficulty == 3:
        max_attempts = 3
    else:
        print("Error: Invalid difficulty")
        return

    print(f"I am thinking of a number between {numb1} and {numb2}. You have {max_attempts} guesses.")

    # Loop for guessing
    attempts_left = max_attempts
    while attempts_left > 0:
        guess = int(input(f"Guess a number ({attempts_left} attempts left): "))

        if guess == random_integer:
            print("Congrats! You got it!")
            break
        elif guess > random_integer:
            print("You went a little high there.")
        else:
            print("You went a little lower than expected.")

        attempts_left -= 1
        if attempts_left == 0:
            print("Game over! You ran out of guesses.")


def main():
    welcome_message()
    numb1, numb2 = get_number_range()
    random_integer = get_random_number(numb1, numb2)
    difficulty = get_difficulty()
    play_game(numb1, numb2, random_integer, difficulty)


if __name__ == "__main__":
    main()
