import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_roulette():
    wins = 0
    print("Welcome to a less dangerous version of Russian roulette")
    while True:
        clear_screen()
        input("Press enter to play...")
        chamber = random.randint(1, 6)
        if chamber == 1:
            print("You died.")
            print(f"Final Score: {wins}")
            input("Press enter to return to the menu.")
            break
        else:
            wins += 1
            print(f"You survived! Round(s) won: {wins}")
            roulette_again = input("Play again? (y/n): ").lower()
            while roulette_again not in ("y", "n"):
                roulette_again = input("Invalid input. Play again? (y/n): ").lower()
            if roulette_again == "n":
                print(f"Your final score was: {wins}")
                input("Press enter to return to the menu.")
                break

def play_number():
    print("Welcome to a number guessing game!")
    print("Try to guess my number between 1 and 10.")
    print("You have three guesses.")
    input("Press enter to continue.")
    
    guesses = 0
    number = random.randint(1, 10)
    
    while True:
        clear_screen()
        print("Guess my number from 1-10")
        if guesses >= 3:
            print(f"Game over! You ran out of guesses. The number was {number}.")
            number_again = input("Play again? (y/n): ").lower()
            if number_again == "y":
                guesses = 0
                number = random.randint(1, 10)
                continue
            else:
                break  
        print(f"Guesses used: {guesses}/3")
        guess = input("Guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            input("Press enter to continue.")
            continue
        if guess < 1 or guess > 10:
            print("Please guess a number between 1 and 10.")
            input("Press enter to continue.")
            continue
        guesses += 1
        if guess == number:
            print("Correct!")
            print(f"The number was {number}")
            number_again = input("Play again? (y/n): ").lower()
            while number_again not in ("y", "n"):
                number_again = input("Invalid input. Play again (y/n): ").lower()
            if number_again == "y":
                guesses = 0
                number = random.randint(1, 10)
            else:
                input("Press enter to return to the menu.")
                break
        else:
            print("Try again!")
            input("Press enter to continue.")

def play_cyoa():
    clear_screen()
    print("You have been tasked with recovering the golden idol.")
    print("The idol was last seen in Lobter Castle.")
    print("However much of the castle was destroyed from the Hampter seige.")
    print("Do what you can to bring the idol back into posession of Lord Honse.")
    print("Even if it costs your life.")
    input("Press enter to continue: ")
    clear_screen()
    print("You stare into down the to the end of what used to be a grand hall.")
    print("Crumbling stone arches and half torn tapestries lines the walls.")
    print("You reach the end of the hall. Do you go left or right?")
    print("'L' for left, 'R' for right.")
    first = input("Enter input here: ").lower()
    while first not in ("l", "r"):
        print("Invalid input. Try again")
        first = input("Enter input here: ").lower()
    if first == "l":
        clear_screen() #Option 1
        print("As you enter trough the oak door, the hinges jam behind you.")
        input("Press enter to continue: ")
        print("Dust floats down from the celing in thick blankets.")
        print("You Died.")
    else:
        clear_screen() #Option 2
        print("Right")
        print("You climb through the hole in the wall, and sit outside enjoying the sunlight.")
        input("Press enter to continue: ")
        print("You were sitting there so long you died of starvation.")


while True:
    try:
        clear_screen()
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("          Games          ")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("1. Russian Roulette")
        print("2. Number Game")
        print("3. Choose Your Own Adventure")
        print("4. Exit")
        
        start = int(input("\nEnter your choice (1-4): "))
        
        if start == 1:
            clear_screen()
            play_roulette()
        elif start == 2:
            clear_screen()
            play_number()
        elif start == 3:
            clear_screen()
            play_cyoa()
        elif start == 4:
            break
        else:
            input("Invalid choice. Press enter to try again.")

    except ValueError:
        input("Invalid input. Please enter a number. Press enter to continue.")

        #the puter has been dignosed, unfortunatley it is terminal