from time import sleep


def guess_game():
    guess_number = "7"
    guess_count = 3
    while guess_count > 0:
        guess = input("Guess: ").strip()
        if guess == guess_number:
            print("You won!")
            sleep(1.5)
            guess_count -= 3
        else:
            if guess_count == 1:
                print("Wrong guess")
                print("You ran out of guesses!")
                sleep(1.5)
                guess_count -= 1

            else:
                print("Wrong guess")
                guess_count -= 1
while True:
    play = input("Type [P] to play or [Q] to quit. Input: ").upper()
    if play == "P":
        print(f"Starting game...")
        sleep(1.5)
        guess_game()
    elif play == "Q":
        print("Exiting game")
        sleep(1.5)
        break
    else:
        print("Invalid input!")
