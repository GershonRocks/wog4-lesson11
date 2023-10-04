from random import randint


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    return compare_results(user_guess, secret_number)


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty):
    guess = input_loop_int(difficulty)
    return guess


def input_loop_int(difficulty):
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit() and 1 <= int(guess) <= difficulty:
            guess = int(guess)
            break
        else:
            print(f"Enter 1 to {difficulty} only!")
    return guess


def compare_results(user_guess, secret_number):
    return user_guess == secret_number
