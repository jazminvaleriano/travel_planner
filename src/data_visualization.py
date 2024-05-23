import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

class DataVisualizer:
    def __init__(self):
        pass

    def visualize_data(self):
        try:
            # Load the itinerary, expenses, and budget data
            itinerary_df = pd.read_csv("itinerary.csv")
            expenses_df = pd.read_csv("expenses.csv")
            budget_df = pd.read_csv("budget.csv")
            
            # Normalize column names
            expenses_df.columns = [col.strip() for col in expenses_df.columns]
            budget_df.columns = [col.strip() for col in budget_df.columns]
            
            # Plot budget vs actual spending
            self.plot_budget_vs_actual(expenses_df, budget_df)
            
            # Plot the timeline of activities
            self.plot_timeline(itinerary_df)
            
            # Plot the breakdown of expenses
            self.plot_expenses(expenses_df)
            
            # Plot daily spending by category
            self.plot_daily_spending_by_category(expenses_df)
            
            # Plot daily over/under budget
            self.plot_daily_over_under_budget(expenses_df, budget_df)
            
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
        print(tabulate(table_data, headers=['Day', 'Activity/Restaurant'], tablefmt='fancy_grid'))

    def plot_expenses(self, expenses_df):
        # Group expenses by category
        category_expenses = expenses_df.groupby('Category')['Amount'].sum().reset_index()

        # Create a pie chart of expenses by category
        plt.figure(figsize=(8, 8))
        plt.pie(category_expenses['Amount'], labels=category_expenses['Category'], autopct='%1.1f%%', startangle=140)
        plt.title('Breakdown of Expenses by Category')
        plt.show()

    def plot_daily_spending_by_category(self, expenses_df):
        # Prepare data
        daily_spending = expenses_df.pivot_table(index='Trip Day', columns='Category', values='Amount', aggfunc='sum').fillna(0)
        
        # Plot
        daily_spending.plot(kind='bar', stacked=True, figsize=(10, 6))
        plt.title('Daily Spending by Category')
        plt.xlabel('Trip Day')
        plt.ylabel('Amount Spent')
        plt.show()

    def plot_budget_vs_actual(self, expenses_df, budget_df):
        # Merge expenses with budget
        comparison_df = pd.merge(expenses_df, budget_df, on=['Trip Day', 'Category'], how='outer').fillna(0)
        comparison_df['Over_Under'] = comparison_df['Budget'] - comparison_df['Amount']
        
        # Plot
        sns.catplot(x='Trip Day', y='Amount', hue='Category', data=comparison_df, kind='bar', height=6, aspect=2)
        plt.title('Budget vs Actual Spending by Category')
        plt.show()


    def plot_daily_over_under_budget(self, expenses_df, budget_df):
        # Merge and calculate over/under
        df = pd.merge(expenses_df, budget_df, on=['Trip Day', 'Category'], how='outer')
