from app import start_play, welcome

welcome()

while True:
    start_play()
    another_round = input("Do you want to play another round? [yes/no]")
    if another_round.lower() == "no":
        break

