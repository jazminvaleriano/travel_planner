import pandas as pd
import numpy as np

class TripPlanner:
    def __init__(self):
        self.trip_details = pd.DataFrame(columns=["destination_city","destination_country","stay_days", "transportation", "budget_range", "activities"])
        self.attractions_data = pd.read_csv("data/attractions.csv")  # Load attractions data
        self.restaurants_data = pd.read_csv("data/restaurants.csv")  # Load restaurants data

    def plan_trip(self):
        print("\nTrip Planner:")
        destination_city = input("Where would you like to go? Enter the name of the city: ")
        stay_days = int(input("How many days do you plan to stay? "))
        # Retrieve country from city
        # Load touristic cities data
        world_cities = pd.read_csv("data/worldcities.csv")
        destination_country = world_cities.loc[world_cities['city'] == destination_city, 'country'].iloc[0]

        # Menu for budget range
        while True:
            print("Select budget range:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            budget_choice = input("Enter your choice (1/2/3): ")
            if budget_choice in ['1', '2', '3']:
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")
        budget_range = ['low', 'med', 'high'][int(budget_choice) - 1]
        
        # Menu for preferred means of transportation
        while True:
            print("Select preferred means of transportation:")
            print("1. Walking/Public Transport")
            print("2. Taxi")
            transportation_choice = input("Enter your choice (1/2): ")
            if transportation_choice in ['1', '2']:
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        transportation = 'walking/public transport' if transportation_choice == '1' else 'taxi'

        activities = []
        while True:
            activity = input("Enter an activity or point of interest (or leave blank to finish): ")
            if not activity:
                break
            activities.append(activity)
        
        trip_data = pd.DataFrame([[destination_city,destination_country, stay_days, transportation, budget_range, activities]], 
                                columns=["destination_city","destination_country","stay_days", "transportation", "budget_range", "activities"])
        self.trip_details = trip_data
        trip_data.to_csv("trip_details.csv", index=False)

        print("\nTrip details saved successfully!")

    def get_trip_details(self):
        return self.trip_details
        
    def get_attractions_for_city(self, city):
        attractions = self.attractions_data[self.attractions_data['city'] == city][:]
        return attractions


    def select_attractions(self, attractions, stay_days):
        # Sort attractions by rating and number of reviews
        sorted_attractions = attractions.sort_values(by=["rating", "num_reviews"], ascending=False).copy()
        
        # Select 2 top attractions per day based on stay duration
        selected_attractions = sorted_attractions.head(2 * stay_days).copy()
        
        # Create trip day series
        trip_days = np.arange(1, stay_days + 1)  # Create an array from 1 to stay_days
    
        # Repeat the array to cover the required number of days
        trip_days = np.tile(trip_days, 2)[:2 * stay_days]  # Repeat twice and truncate if necessary
    
        # Add trip day column
        selected_attractions['trip_day'] = trip_days

        return selected_attractions

    
    def get_restaurants_for_city(self, city, budget_range):
        restaurants = self.restaurants_data[self.restaurants_data['city'] == city][:]
        
        # Filter restaurants based on budget_range
        if budget_range == 'low':
            restaurants = restaurants[restaurants['price_range'] == '$']
        elif budget_range == 'med':
            restaurants = restaurants[restaurants['price_range'].isin(['$', '$$'])]
        # For high budget_range, no filtering needed!
        
        return restaurants

    def select_restaurants(self, restaurants, stay_days):
        # Sort restaurants by rating and number of reviews
        sorted_restaurants = restaurants.sort_values(by=["rating", "num_reviews"], ascending=False)
        
        # Select 2 top restaurants per day based on stay duration
        selected_restaurants = sorted_restaurants.head(2 * stay_days).copy()  # Make a copy
        
        # Create trip day series
        trip_days = np.arange(1, stay_days + 1)  # Create an array from 1 to stay_days
    
        # Repeat the array to cover the required number of days
        trip_days = np.tile(trip_days, 2)[:2 * stay_days]  # Repeat twice and truncate if necessary
    
        # Add trip day column
        selected_restaurants['trip_day'] = trip_days

        return selected_restaurants
    
    def generate_itinerary(self):
        suggestions = []
        trip_row = self.trip_details.iloc[-1]  # Accessing the most recent trip details
        destination_city = trip_row['destination_city']
        destination_country = trip_row['destination_country']
        stay_days = trip_row['stay_days']
        budget_range = trip_row['budget_range']
        
        # Get attractions for the destination city
        attractions = self.get_attractions_for_city(destination_city)
        selected_attractions = self.select_attractions(attractions, stay_days)
        for _, attraction in selected_attractions.iterrows():
            suggestions.append(["Attraction", attraction['name'], attraction['location'], attraction['price_range'], attraction['rating'], attraction['trip_day']])

        # Get restaurants for the destination city based on budget range
        restaurants = self.get_restaurants_for_city(destination_city, budget_range)
        selected_restaurants = self.select_restaurants(restaurants, stay_days)
        for _, restaurant in selected_restaurants.iterrows():
            suggestions.append(["Restaurant",destination_country, restaurant['name'], restaurant['location'], restaurant['price_range'], restaurant['rating'], restaurant['trip_day']])
        
        # Convert suggestions to DataFrame
        suggestions_df = pd.DataFrame(suggestions, columns=["type", "Country","suggestion", "location", "price range", "rating", "trip_day"])
    
        # Merge with the DataFrame containing country-wise meal prices
        meal_prices_df = pd.read_csv("data/CountrySpecific_RestaurantCost.csv")  
        suggestions_with_costs = pd.merge(suggestions_df, meal_prices_df, left_on='location', right_on='Country', how='left')
            
        # Calculate estimated cost per meal based on price range and country
        def calculate_estimated_cost(row):
            if row['price range'] == 'high':
                return row['Price'] * 2.5  
            elif row['price range'] == 'med':
                return row['Price'] * 1.5  
            else:
                return row['Price']  # DataFrame contains data for low budget meals
        
        suggestions_with_costs['estimated_cost_per_meal'] = suggestions_with_costs.apply(calculate_estimated_cost, axis=1)
        
        # Save itinerary to a CSV file
        suggestions_with_costs.to_csv("itinerary.csv", index=False)
        print(f"\nItinerary saved to itinerary.csv!")

        return suggestions_with_costs
