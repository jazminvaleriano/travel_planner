# Exception Handling in TripPlanner

## Overview

This document describes the exceptions handled in our project to ensure robust and user-friendly operation.

## Exceptions

### City Validation Exception

**Purpose and rationale**: Ensure the input city exists in the dataset to maintain data integrity and provide a smooth user experience. We use restaurants.csv as the limiting dataframe, as this is the dataset with the least number of cities availables in our data folder.

**Implementation**:

```python
def plan_trip(self):
    print("\nTrip Planner:")
    
    available_cities = self.restaurants_data['city'].unique()
    
    while True:
        destination_city = input("Where would you like to go? Enter the name of the city: ")
        if destination_city in available_cities:
            break
        else:
            print(f"Error: {destination_city} is not available in our data. Please choose a different city.")
    
    stay_days = int(input("How many days do you plan to stay? "))
    world_cities = pd.read_csv("data/worldcities.csv")
    destination_country = world_cities.loc[world_cities['city'] == destination_city, 'country'].iloc[0]
    # Rest of the method...
```

### Category Validation Exception
***Purpose and rationale***: Restrict expense categories to a predefined list to ensure data consistency and prevent errors. We want to ensure expense categories can be matched to budget categories to allow for comparison.

***Implementation***:

    ```python
    def track_expense(self):
        allowed_categories = ['food', 'transport', 'activities', 'others']
        
        try:
            trip_day = float(input("Enter the trip day: "))
            category = input("Enter the category of expense (Food, Transport, Activities, Others): ").strip().lower()
            
            if category not in [cat.lower() for cat in allowed_categories]:
                raise ValueError(f"Invalid category. Allowed categories are: {', '.join([cat.capitalize() for cat in allowed_categories])}")
            
            amount = float(input(f"Enter the amount spent on {category.capitalize()}: "))
            
            if self.expenses.empty:
                self.expenses = pd.DataFrame({"Trip Day": [trip_day], "Category": [category.capitalize()], "Amount": [amount]})
            else:
                new_expense = pd.DataFrame({"Trip Day": [trip_day], "Category": [category.capitalize()], "Amount": [amount]})
                self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
            
            self.expenses.to_csv('expenses.csv', index=False)
            print(f"Added expense for: {category.capitalize()} - ${amount} on trip day {trip_day} successfully. See expense.csv for details per category and per day.")
        except ValueError as e:
            print(e)
    ```
