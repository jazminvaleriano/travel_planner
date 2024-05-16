import pandas as pd
import os

class BudgetManager:
    def __init__(self):
        # Setting up an empty budget and empty dataframe for expenses
        self.budget = None
        self.expenses = pd.DataFrame(columns=["Trip Day","Category", "Amount"])

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
            choice = input("Do you want to use the generated itinerary? (yes/no): ").lower()
            
            if choice == 'yes':
                # Check if itinerary.csv exists
                if os.path.isfile("itinerary.csv"):
                    # If the file exists, read it
                    itinerary_df = pd.read_csv("itinerary.csv")
                    print("Itinerary loaded successfully.")
                    # Extract the total budget by category from the loaded itinerary
                    budget_activities = itinerary_df[(itinerary_df['category'] == 'Attraction') | (itinerary_df['category'] == 'Activity defined by user')]["estimated_cost"].sum()
                    budget_food = itinerary_df[itinerary_df['category'] == 'Restaurant']["estimated_cost"].sum()

                else:
                    budget_activities = float(input("Enter your total budget for activities the trip: "))
                    budget_food = float(input("Enter your total budget for food the trip: "))

            else:
                budget_activities = float(input("Enter your total budget for activities the trip: "))
                budget_food = float(input("Enter your total budget for food the trip: "))
        
            # Read trip details to get destination country and stay days
            trip_details_df = pd.read_csv("trip_details.csv")
            destination_country = trip_details_df['destination_country'].iloc[0]
            stay_days = trip_details_df['stay_days'].iloc[0]
            transportation_mode = trip_details_df['transportation'].iloc[0]

            # Read transportation cost for public transport based on destination country

            if transportation_mode.lower() == 'walking/public transport':
                transportation_cost_df = pd.read_csv("data/CountrySpecific_TransportationCost.csv")
                transportation_cost = transportation_cost_df.loc[transportation_cost_df['Country'] == destination_country, 'Public Transportation Cost (USD)'].iloc[0]
            else:
                transportation_cost = 100  # Assume $100 per day if transportation mode is taxi 
                
            # Calculate transportation budget
            budget_transportation = transportation_cost * stay_days * 4  # Assuming an average of 4 one way rides per day for public transport
            
            # Store budget details in a DataFrame
            budget_data = {
                'Category': ['Activities', 'Food', 'Transportation'],  # Include Transportation category
                'Budget': [budget_activities, budget_food, budget_transportation]  # Include transportation_budget
            }
            budget_df = pd.DataFrame(budget_data)

            # Save the budget DataFrame to a CSV file
            budget_df.to_csv('budget.csv', index=False)

            self.budget_food = budget_food
            self.budget_activities = budget_activities
            self.budget_transportation = budget_transportation
            
            # Calculate total budget correctly
            self.budget = sum([budget_activities, budget_food, budget_transportation])

            print(f"Budget of ${self.budget} created successfully. See budget.csv for details per category.")
        except ValueError:
            print("Invalid input. Please enter a number for the budget.")

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


