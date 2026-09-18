import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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

#hamburger



play_cyoa()