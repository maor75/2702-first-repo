import random
def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Choose a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Invalid input, please enter a number between 1 and {difficulty}")
        except ValueError:
            print("Invalid input, please enter a number")


def compare_results(secret_number, guess):
    if guess == secret_number:
        return True
    else:
        return False


def play(difficulty):
    secret_number = generate_number(difficulty)
    while True:
        guess = get_guess_from_user(difficulty)
        if compare_results(secret_number, guess):
            print("Congratulations, you guessed the secret number:")
        else:
            print(f"Sorry, the secret number was :  {generate_number(difficulty)} ")
