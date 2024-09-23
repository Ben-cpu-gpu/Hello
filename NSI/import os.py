import os
import random

def russian_roulette(chambers=6):
    bullet_chamber = random.randint(1, chambers)  # randomly select a chamber for the bullet

    print("Welcome to Russian Roulette!")
    print(f"There are {chambers} chambers in the revolver.")
    print("Pull the trigger? (y/n)")

    response = input().lower()

    if response == 'y':
        chamber = random.randint(1, chambers)  # simulate pulling the trigger
        print(f"You pulled the trigger and got chamber {chamber}!")

        if chamber == bullet_chamber:
            print("You lost! The computer will shut down in 10 seconds.")
            os.system("shutdown /s /c ntm /t 30")  # shut down the computer (Windows only)
        else:
            print("You survived! Congratulations!")
            if chambers > 1:
                play_again = input("Do you want to play again? (y/n): ")
                if play_again.lower() == 'y':
                    russian_roulette(chambers - 1)  # recursive call to play again with 1 less chamber
                else:
                    print("Thanks for playing!")
            else:
                print("You've played with the last chamber! Game over.")
    else:
        print(f"The bullet was in chamber {bullet_chamber}.")
        if bullet_chamber == 1:
            print("You would have lost if you pulled the trigger!")
        else:
            print("You would have survived if you pulled the trigger!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            russian_roulette(chambers)  # recursive call to play again with the same number of chambers
        else:
            print("Thanks for playing!")

russian_roulette()