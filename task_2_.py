class Trip:
    def __init__(self, budget):
        self.initial_budget = budget
        self.remaining_budget = budget
        self.expenses = {
            'accommodation': 0,
            'transportation': 0,
            'meals': 0,
            'activities': 0
        }

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
            self.remaining_budget -= amount
            print(f"You spent {amount} in the {category} category.")
        else:
            print("Invalid category.")

    def display_remaining_budget(self):
        print(f"Remaining budget: {self.remaining_budget}")

    def display_expenses(self):
        for category, amount in self.expenses.items():
            print(f"{category.capitalize()} : {amount}")

# Function to input a valid amount
def input_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid amount.")

# Main function
def main():
    initial_budget = float(input("Enter your travel budget: "))
    trip = Trip(initial_budget)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Display remaining budget")
        print("3. Display expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nChoose expense category:")
            print("1. Accommodation")
            print("2. Transportation")
            print("3. Meals")
            print("4. Activities")
            category = input("Enter your choice: ")
            amount = input_amount()
            if category == "1":
                trip.add_expense('accommodation', amount)
            elif category == "2":
                trip.add_expense('transportation', amount)
            elif category == "3":
                trip.add_expense('meals', amount)
            elif category == "4":
                trip.add_expense('activities', amount)
            else:
                print("Invalid choice.")
        elif choice == "2":
            trip.display_remaining_budget()
        elif choice == "3":
            trip.display_expenses()
        elif choice == "4":
            print("Thank you for using our program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
class Trip:
    def __init__(self, budget):
        self.initial_budget = budget
        self.remaining_budget = budget
        self.expenses = {
            'accommodation': 0,
            'transportation': 0,
            'meals': 0,
            'activities': 0
        }

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
            self.remaining_budget -= amount
            print(f"You spent {amount} in the {category} category.")
        else:
            print("Invalid category.")

    def display_remaining_budget(self):
        print(f"Remaining budget: {self.remaining_budget}")

    def display_expenses(self):
        for category, amount in self.expenses.items():
            print(f"{category.capitalize()} : {amount}")

# Function to input a valid amount
def input_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid amount.")

# Main function
def main():
    initial_budget = float(input("Enter your travel budget: "))
    trip = Trip(initial_budget)

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Display remaining budget")
        print("3. Display expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nChoose expense category:")
            print("1. Accommodation")
            print("2. Transportation")
            print("3. Meals")
            print("4. Activities")
            category = input("Enter your choice: ")
            amount = input_amount()
            if category == "1":
                trip.add_expense('accommodation', amount)
            elif category == "2":
                trip.add_expense('transportation', amount)
            elif category == "3":
                trip.add_expense('meals', amount)
            elif category == "4":
                trip.add_expense('activities', amount)
            else:
                print("Invalid choice.")
        elif choice == "2":
            trip.display_remaining_budget()
        elif choice == "3":
            trip.display_expenses()
        elif choice == "4":
            print("Thank you for using our program. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()