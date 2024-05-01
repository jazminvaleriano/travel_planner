# destinations.py

def print_options():
    # Print travel options
    print("Travel Options")
    print("--------------")
    print("1. Rome")
    print("2. Berlin")
    print("3. Vienna")
    print("")

def get_choice():
    # Get destination choice
    while True:
        try:
            choice = int(input("Where would you like to go? "))
            if (choice < 1) or (choice > 3):
                print("Please select a choice between 1 and 3.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            return choice


def get_info(choice):
    # Use numeric choice to look up destination info
    # Rates are listed in euros per day
    # Choice 1: Rome at €45/day

    if (choice == 1):
        return "Rome", 45

    # Choice 2: Berlin at €18/day
    elif (choice == 2):
        return "Berlin", 18

    # Choice 3: Vienna, €34/day
    elif (choice == 3):
        return "Vienna", 34