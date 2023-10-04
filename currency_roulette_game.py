from random import randint
from currency_converter import CurrencyConverter


def play(difficulty):
    return is_list_equal(difficulty)


def get_money_interval(difficulty):
    exchange_rate = get_currency_rate()
    secret_number = randint(1, difficulty) * exchange_rate
    # print(f"Secret Number {secret_number}")
    return secret_number


def get_guess_from_user():
    guess = input_loop_float()
    return guess


def input_loop_float():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit() or guess.replace(".", "").isnumeric():
            guess = float(guess)
            break
        else:
            print(f"Enter a valid number as a guess!")
    return guess


def is_list_equal(difficulty):
    secret_number = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    return user_guess - (10-difficulty) <= secret_number <= user_guess + (10-difficulty)


def get_currency_rate():
    currency_converter = CurrencyConverter()
    currency_rate = currency_converter.convert(1, "USD", "ILS")
    print(currency_rate)
    return currency_rate
