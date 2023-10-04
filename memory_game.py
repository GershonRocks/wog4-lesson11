from random import randint
import os
from time import sleep


def play(difficulty):
    secret_list = generate_sequence(difficulty)
    print("Enter your guesses: ")
    user_list = get_list_from_user(difficulty)
    return is_list_equal(user_list, secret_list)


def generate_sequence(difficulty):
    secret_list = []
    for num in range(difficulty):
        secret_list.append(randint(1, 101))
    print(f"Take a brief look at the number: {secret_list}")
    sleep(2)
    clear_terminal()
    return secret_list


def get_list_from_user(difficulty):
    user_list = []
    for num in range(difficulty):
        input_loop_append(user_list)
    return user_list


def input_loop_append(user_list):
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit() and 1 <= int(guess) <= 101:
            guess = int(guess)
            user_list.append(guess)
            break
        else:
            print("Enter 1 to 101 only!")


def is_list_equal(user_list, secret_list):
    return user_list == secret_list


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * 100)

