import pandas as pd

class BudgetManager:
    def __init__(self):
        # Setting up an empty budget and empty dataframe for expenses
        self.budget = None
        self.expenses = pd.DataFrame(columns=["Category", "Amount"])

    def manage_budget(self):
        # Create a menu for budget management and for handling the user's choice
        while True:
            print("\nBudget Management Menu:")
            print("1. Create Budget")
            print("2. Track Expenses")
            print("3. View Budget and Expenses")
            print("4. Return to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.create_budget()  # Create a new budget
            elif choice == '2':
                self.track_expense()  # Track a new expense
            elif choice == '3':
                self.view_budget_and_expenses()  # Show the budget and current expenses
            elif choice == '4':
                break  # Return to the main menu
            else:
                print("Invalid choice. Please enter a number between 1 & 4.")

    def create_budget(self):
        # Function to create a budget for the trip
        try:
            total_budget = float(input("Enter your total budget for the trip: "))
            self.budget = total_budget
            print(f"Budget of ${total_budget} created successfully.")
        except ValueError:
            print("Invalid input. Please enter a number for the budget.")

    def track_expense(self):
        # Request the user to enter details of a new expense
        try:
            category = input("Enter the category of expense (e.g., Accommodation, Food, Transport, etc.): ")
            amount = float(input(f"Enter the amount spent on {category}: "))
            # Add the expense to the expenses DataFrame
            new_expense = pd.DataFrame({"Category": [category], "Amount": [amount]})
            self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
            print(f"Added expense: {category} - ${amount}")
        except ValueError:
            print("Invalid input. Please enter a number for the amount.")

    def view_budget_and_expenses(self):
        # Show the user the budget and tracked expenses
        if self.budget is None:
            print("No budget created yet. Please create a budget first.")
            return
        
        print("\n--- Budget and Expenses ---")
        print(f"Total Budget: ${self.budget}")
        
        if self.expenses.empty:
            print("No expenses have been recorded yet.")
        else:
            print("\nTracked Expenses:")
            print(self.expenses.to_string(index=False))

        total_spent = self.expenses["Amount"].sum()
        print(f"\nTotal Spent: ${total_spent}")
        print(f"Remaining Budget: ${self.budget - total_spent}")


