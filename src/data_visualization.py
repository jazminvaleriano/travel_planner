import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

class DataVisualizer:
    def __init__(self):
        pass

    def visualize_data(self):
        try:
            # Load the itinerary and expenses data
            itinerary_df = pd.read_csv("itinerary.csv", dtype={"trip_day": int})
            expenses_df = pd.read_csv("expenses.csv")
            
            # Plot the timeline of activities
            self.plot_timeline(itinerary_df)
            
            # Plot the breakdown of expenses
            self.plot_expenses(expenses_df)
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def plot_timeline(self, itinerary_df):

        # Extract data for the timeline
        days = itinerary_df['trip_day']
        activities = itinerary_df['suggestion']

        # Create a timeline plot
        plt.figure(figsize=(12, 6))
        plt.plot(days, activities, marker='o')
        plt.xlabel('Trip Day')
        plt.ylabel('Activity')
        plt.title('Timeline of Planned Activities')
        plt.grid(True)
        plt.show()

        # Display timeline in table in addition to the plot
        table_data = []
        for index, row in itinerary_df.iterrows():
            table_data.append([row['trip_day'], row['suggestion']])
        
        # Print the table
        print(tabulate(table_data, headers=['Day', 'Activity'], tablefmt='fancy_grid'))

    def plot_expenses(self, expenses_df):
        # Group expenses by category
        category_expenses = expenses_df.groupby('Category')['Amount'].sum().reset_index()

        # Create a pie chart of expenses by category
        plt.figure(figsize=(8, 8))
        plt.pie(category_expenses['Amount'], labels=category_expenses['Category'], autopct='%1.1f%%', startangle=140)
        plt.title('Breakdown of Expenses by Category')
        plt.show()

