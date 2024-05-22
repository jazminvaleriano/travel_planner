import matplotlib.pyplot as plt
import pandas as pd

# Sample trip data
trip_data = {
    'activities': [
        {'name': 'Flight to Paris', 'start_time': '2023-06-01 10:00', 'end_time': '2023-06-01 14:00'},
        {'name': 'Eiffel Tower Visit', 'start_time': '2023-06-02 09:00', 'end_time': '2023-06-02 11:00'},
        {'name': 'Louvre Museum', 'start_time': '2023-06-03 12:00', 'end_time': '2023-06-03 15:00'},
    ],
    'expenses': [
        {'category': 'Transportation', 'amount': 300},
        {'category': 'Accommodation', 'amount': 600},
        {'category': 'meals', 'amount': 150},
        {'category': 'activities', 'amount': 100},
    ]
}

def plot_activity_timeline(activities):
    # Convert activity times to pandas datetime
    for activity in activities:
        activity['start_time'] = pd.to_datetime(activity['start_time'])
        activity['end_time'] = pd.to_datetime(activity['end_time'])

    # Create a DataFrame
    df = pd.DataFrame(activities)

    # Plot the timeline
    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, activity in df.iterrows():
        ax.plot([activity['start_time'], activity['end_time']], [idx, idx], marker='o')

    ax.set_yticks(range(len(df)))
    ax.set_yticklabels(df['name'])
    ax.set_xlabel('Time')
    ax.set_title('Activity Timeline')
    plt.grid(True)
    plt.show()

def plot_expense_breakdown(expenses):
    # Create a DataFrame
    df = pd.DataFrame(expenses)

    # Plot the pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    df.groupby('category').sum().plot(kind='pie', y='amount', ax=ax, autopct='%1.1f%%')
    ax.set_ylabel('')
    ax.set_title('Expense Breakdown')
    plt.show()

# Example usage
plot_activity_timeline(trip_data['activities'])
plot_expense_breakdown(trip_data['expenses'])
