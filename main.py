# Programmers:  Korede Oni
# Course:  CS151, Dr. Yalew
# Due Date: 11/7/24
# Programming Assignment:  03
# Problem Statement:  Create a program to display ASCII art and string decorations to the user.
# Data In: Whether the user would like to have a circle, set of lines with a character or a random design displayed to them,
#          What character the user want to repeat, how many lines they want to print, how many columns they want to print
#          When the user wants to quit
# Data Out: The ASCII art that the user selected
# Credits: Nothing other than class :)


# Import random module
import random


# Print circle
def print_circle():
    print("        ---------  ")
    print(r"      /           \ ")
    print(r"    /               \ ")
    print("   |                 | ")
    print(r"    \               / ")
    print(r"      \           /  ")
    print("        ---------  ")

# Print lines of a certain character
def print_lines():
    character = str(input("What character do you want to see repeated? "))
    columns = int(input("How many times should this character be printed on one line? "))
    while columns <= 0:
        columns = int(input("You have more than 0 columns for printing. How many times should this character be printed on one line? "))
    row = int(input("How many rows of these lines would you like to be printed? "))
    while row <= 0:
        row = int(input("You must have more than 0 rows for printing. How many rows of these lines would you like to be printed? "))
    count = 0
    print("")
    while count < row:
        print(character * columns)
        count += 1

# Prints a random piece of art
def print_random():
    random_choice = random.randint(1, 3)
    if random_choice == 1:
        hand_mid = "|               |"
        end_left = r"\ "
        end_right = " /"
        space_before = 1
        space_between = 11
        loop_mid = 2
        print("You get... the right hand")
        print("       __   ")
        print("    --|  |--")
        print(" __|  |  |  |")
        print("/" + "  |" * 4)
        print("|" + "  |" * 4+ " _")
        print(r"|  |        |   \ ")
        while loop_mid > 0:
            print(hand_mid)
            loop_mid -= 1
        while space_before <= 2:
            print(" " * space_before + end_left + " " * space_between + end_right)
            space_before += 1
            space_between -= 2
        print("    - - - - -")
    elif random_choice == 2:
        print("You get... an elephant!")
        print("       ---- (    )")
        print(r"     / *    \ _ /    _________")
        print(r"    /         -------          \   ")
        print(r"   /   ____                     \ --- ")
        print(r"   |   |    \          ___       |   \ ")
        print(r"   |   |     \        |   |      |     --** ")
        print(r"    \ /       |       |   |      |")
        print("              |       |   |      |")
        print("             /        |  /       |")
        print("             ---------   --------")
    elif random_choice == 3:
        four_slash = "/  /"
        four_straight = "|  |"
        space_before = 5
        space_between = 4
        space_end = 2
        print("You get... the mighty number 4!")
        print("       _________  ")
        while space_before > 0:
            print(" " * space_before + four_slash + " " * space_between + four_straight)
            space_before -= 1
            space_between += 1
        print("|  |         |  |")
        print("|__|_________|__|___.")
        print("|__|_________|__|___|")
        while space_end > 0:
            print(" " * 13 + four_straight)
            space_end -= 1
        print("             |__|")

# Main function
def main():
    print("Welcome to our ASCII Art Display program!\n"
          "Here, we can print a few different things. We hope you'll find some interesting stuff here.\n"
          "Let's begin!")
    print("")
    choice = str(input("Choose an option to print:\n"
                       "To print a circle, please type circle"
                       "To print a character on a set of lines, please type lines\n"
                       "To print a random piece of art, please type random\n"
                       "To quit, please type quit\n"
                       "Choose your option: "))
    print("")
    choice = choice.lower()
    while choice != "circle" and choice != "lines" and choice != "random" and choice != "quit":
        choice = str(input("Invalid option, please try again\n"
                           "Choose an option to print:\n"
                           "To print a circle, please type circle\n"
                           "To print a character on a set of lines, please type lines\n"
                           "To print a random piece of art, please type random\n"
                           "To quit, please type quit\n"
                           "Choose your option: "))
        print("")
        choice = choice.lower()
    while choice != "quit":
        if choice == "circle":
            print_circle()
            print("")
        elif choice == "lines":
            print_lines()
            print("")
        elif choice == "random":
            print_random()
            print("")
        choice = str(input("Choose an option to print:\n"
                           "To print a circle, please type circle\n"
                           "To print a character on a set of lines, please type lines\n"
                           "To print a random piece of art, please type random\n"
                           "To quit, please type quit\n"
                           "Choose your option: "))
        print("")
        choice = choice.lower()
        while choice != "circle" and choice != "lines" and choice != "random" and choice != "quit":
            choice = str(input("Invalid option, please try again\n"
                               "Choose an option to print:\n"
                               "To print a circle, please type circle\n"
                               "To print a character on a set of lines, please type lines\n"
                               "To print a random piece of art, please type random\n"
                               "To quit, please type quit\n"
                               "Choose your option: "))
            print("")
            choice = choice.lower()

    print("Thank you for using our ASCII Art Display program!")

# Call main
main()