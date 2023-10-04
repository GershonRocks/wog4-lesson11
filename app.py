import currency_roulette_game
import guess_game
import memory_game

from score import add_score

def welcome():
    username = input("Enter your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    print("""
    Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 seconds and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    """)
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit() and 1 <= int(choice) <= 3:
            choice = int(choice)
            break
        else:
            print("Enter 1 to 3 only!")

    while True:
        difficulty = input("Enter difficulty [1 - 5]: ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            difficulty = int(difficulty)
            break
        else:
            print("Enter 1 to 5 only!")

    if choice == 1:
        memory_game_play(difficulty)
    elif choice == 2:
        guess_game_play(difficulty)
    elif choice == 3:
        currency_roulette_play(difficulty)


def play_game_executor(game, difficulty):
    if game.play(difficulty):
        print("You Win")
        add_score(difficulty)
    else:
        print("You Lose")


def memory_game_play(difficulty):
    play_game_executor(memory_game, difficulty)


def guess_game_play(difficulty):
    play_game_executor(guess_game, difficulty)


def currency_roulette_play(difficulty):
    play_game_executor(currency_roulette_game, difficulty)
