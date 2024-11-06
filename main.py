def print_circle():
    print("       ---------  ")
    print(r"     /           \ ")
    print(r"   /               \ ")
    print(r"  |                 | ")
    print(r"   \               / ")
    print(r"     \           /  ")
    print("       ---------  ")

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

def print_random():
    return 0

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
    while choice != "circle" and choice != "line" and choice != "random" and choice != "quit":
        choice = str(input("Invalid option, please try again\n"
                           "Choose an option to print:\n"
                           "To print a circle, please type circle"
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
                           "To print a circle, please type circle"
                           "To print a character on a set of lines, please type lines\n"
                           "To print a random piece of art, please type random\n"
                           "To quit, please type quit\n"
                           "Choose your option: "))
        print("")
        choice = choice.lower()
        while choice != "circle" and choice != "line" and choice != "random" and choice != "quit":
            choice = str(input("Invalid option, please try again\n"
                               "Choose an option to print:\n"
                               "To print a circle, please type circle"
                               "To print a character on a set of lines, please type lines\n"
                               "To print a random piece of art, please type random\n"
                               "To quit, please type quit\n"
                               "Choose your option: "))
            print("")
            choice = choice.lower()

    print("Thank you for using our ASCII Art Display program!")

main()