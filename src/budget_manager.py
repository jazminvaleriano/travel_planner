import pandas as pd
import os

class BudgetManager:
    def __init__(self):
        # Setting up an empty budget and empty dataframe for expenses
        self.budget = None
        self.expenses = pd.DataFrame(columns=["Trip Day", "Category", "Amount"])

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
            # Ask the user if they want to use the generated itinerary or enter manually
            choice = input("Do you want to use the generated itinerary to get a budget estimate? If not, the costs need to be entered manually (yes/no): ").lower()
            
            if choice == 'yes':
                # Check if itinerary.csv exists
                if os.path.isfile("itinerary.csv"):
                    # If the file exists, read it
                    itinerary_df = pd.read_csv("itinerary.csv")
                    print("Itinerary loaded successfully.")
                    budget_days = []
                    trip_days = sorted(itinerary_df['trip_day'].unique())
                    for day in trip_days:
                        day_df = itinerary_df[itinerary_df['trip_day'] == day]
                        for category in ['Attraction', 'Restaurant']:
                            category_budget = day_df[day_df['category'] == category]['estimated_cost'].sum()
                            budget_days.append({'Trip Day': day, 'Category': category, 'Budget': category_budget})
                    
                    # Read trip details to get destination country, stay days, and transportation mode
                    trip_details_df = pd.read_csv("trip_details.csv")
                    destination_country = trip_details_df['destination_country'].iloc[0]
                    stay_days = trip_details_df['stay_days'].iloc[0]
                    transportation_mode = trip_details_df['transportation'].iloc[0]
                    
                    # Calculate transportation budget
                    if transportation_mode.lower() == 'walking/public transport':
                        transportation_cost_df = pd.read_csv("data/CountrySpecific_TransportationCost.csv")
                        transportation_cost = transportation_cost_df.loc[transportation_cost_df['Country'] == destination_country, 'Public Transportation Cost (USD)'].iloc[0]
                        budget_transportation = transportation_cost * stay_days * 4  # Assuming an average of 4 one way rides per day for public transport
                    else:
                        budget_transportation = 100 * stay_days  # Assume $100 per day if transportation mode is taxi
                    
                    for day in range(1, stay_days + 1):
                        budget_days.append({'Trip Day': day, 'Category': 'Transportation', 'Budget': budget_transportation / stay_days})
                
                else:
                    print("Itinerary file does not exist. Please enter the budget manually.")
                    return

            else:
                budget_activities = float(input("Enter your total budget for activities for the trip: "))
                budget_food = float(input("Enter your total budget for food for the trip: "))
                budget_transportation = float(input("Enter your total budget for transportation for the trip: "))

                # Read trip details to get stay days
                trip_details_df = pd.read_csv("trip_details.csv")
                stay_days = trip_details_df['stay_days'].iloc[0]

                # Create budget per day
                budget_days = []
                for day in range(1, stay_days + 1):
                    budget_days.append({'Trip Day': day, 'Category': 'Activities', 'Budget': budget_activities / stay_days})
                    budget_days.append({'Trip Day': day, 'Category': 'Food', 'Budget': budget_food / stay_days})
                    budget_days.append({'Trip Day': day, 'Category': 'Transportation', 'Budget': budget_transportation / stay_days})
            
            # Convert to DataFrame and save to CSV
            budget_df = pd.DataFrame(budget_days)
            budget_df.to_csv('budget.csv', index=False)

            # Summarize the budget
            self.budget = budget_df['Budget'].sum()

            print(f"Budget created successfully. See budget.csv for details per category and per day.")
        except ValueError:
            print("Invalid input. Please enter a number for the budget.")

    def track_expense(self):
        # Request the user to enter details of a new expense
        try:
            trip_day = float(input("Enter the trip day: "))
            category = input("Enter the category of expense (e.g., Accommodation, Food, Transport, etc.): ")
            amount = float(input(f"Enter the amount spent on {category}: "))
            
            # Check if expenses DataFrame is empty
            if self.expenses.empty:
                # If expenses DataFrame is empty, directly assign the new_expense DataFrame
                self.expenses = pd.DataFrame({"Trip Day": [trip_day], "Category": [category], "Amount": [amount]})
            else:
                # If expenses DataFrame is not empty, concatenate new_expense DataFrame
                new_expense = pd.DataFrame({"Trip Day": [trip_day], "Category": [category], "Amount": [amount]})
                self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
            
            # Save expenses to expenses.csv
            self.expenses.to_csv('expenses.csv', index=False)
                
            print(f"Added expense for: {category} - ${amount} on trip day {trip_day} successfully. See expense.csv for details per category and per day.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount for the expense.")
            
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