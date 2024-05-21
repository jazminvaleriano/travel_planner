# Exception Handling in TripPlanner

## Rationale for Exception Handling

In the TripPlanner class, we have implemented an exception handling block to ensure that users can only input cities that are available in the data/restaurants.csv file, as this is the dataset with the least number of cities availables in our data folder. Having this restriction is important for several reasons:

1. *Data Integrity*: Ensuring that the input city exists in our dataset helps maintain the integrity of the trip planning process. If a user enters a city that is not in our data, the program might fail when trying to access non-existent data, leading to crashes or incorrect outputs.

2. *User Experience*: By handling this exception, we can provide meaningful feedback to the user. Instead of the program crashing or producing incorrect results, the user is informed that the city is not available and prompted to enter a different city.

3. *Error Prevention*: Preventing invalid inputs at an early stage helps avoid potential errors later in the program. This makes the code more robust and easier to maintain.

## Implementation Details

The exception handling is implemented in the plan_trip method. Here's a snippet of the relevant code:

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