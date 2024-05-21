import pandas as pd
import numpy as np

class CityNotFoundError(Exception):
    pass

class TripPlanner:
    def __init__(self):
        self.trip_details = pd.DataFrame(columns=["destination_city", "destination_country", "stay_days", "transportation", "budget_range", "activities"])
        self.attractions_data = pd.read_csv("data/attractions.csv")  # Load attractions data
        self.restaurants_data = pd.read_csv("data/restaurants.csv")  # Load restaurants data

    def plan_trip(self):
        print("\nTrip Planner:")
        
        # Normalize city names to lowercase for comparison
        available_cities = self.restaurants_data['city'].str.lower().unique()
        available_cities = self.attractions_data['city'].str.lower().unique()
        
        
        while True:
            try:
                destination_city = input("Where would you like to go? Enter the name of the city: ").strip()
                if destination_city.lower() not in available_cities: # Converting to lowercase to allow for search in dataset
                    raise CityNotFoundError(f"Error: {destination_city} is not available in our data. Please choose a different city.")
                break
            except CityNotFoundError as e:
                print(e)
        
        stay_days = int(input("How many days do you plan to stay? "))
        
        # Retrieve country from city using a case-insensitive match
        world_cities = pd.read_csv("data/worldcities.csv")
        destination_country = world_cities.loc[world_cities['city'].str.lower() == destination_city.lower(), 'country'].iloc[0]

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
        activities_costs = []
        activities_days = []

        while True:
            activity = input("Enter an activity or point of interest (or leave blank to finish): ")
            if not activity:
                break
            activities.append(activity)
            cost = input(f"Enter the estimated cost in USD for '{activity}': ")
            trip_day = int(input(f"On which day of your trip do you plan to do '{activity}'?(1,2,3..etc) "))
            activities_costs.append(cost)
            activities_days.append(trip_day)
        
        trip_data = pd.DataFrame([[destination_city, destination_country, stay_days, transportation, budget_range, activities, activities_costs, activities_days]], 
                                 columns=["destination_city", "destination_country", "stay_days", "transportation", "budget_range", "activities", "activities_costs", "activities_days"])
        self.trip_details = trip_data
        trip_data.to_csv("trip_details.csv", index=False)

        print("\nTrip details saved successfully!")

    def get_trip_details(self):
        return self.trip_details
        
    def get_attractions_for_city(self, city):
        attractions = self.attractions_data[self.attractions_data['city'].str.lower() == city.lower()][:]
        return attractions

    def select_attractions(self, attractions, stay_days):
        sorted_attractions = attractions.sort_values(by=["rating", "num_reviews"], ascending=False).copy()
        selected_attractions = sorted_attractions.head(2 * stay_days).copy()
        trip_days = np.arange(1, stay_days + 1)
        trip_days = np.tile(trip_days, 2)[:2 * stay_days]
        selected_attractions['trip_day'] = trip_days
        return selected_attractions
    
    def get_restaurants_for_city(self, city, budget_range):
        restaurants = self.restaurants_data[self.restaurants_data['city'].str.lower() == city.lower()][:]
        if budget_range == 'low':
            restaurants = restaurants[restaurants['price_range'] == '$']
        elif budget_range == 'med':
            restaurants = restaurants[restaurants['price_range'].isin(['$', '$$'])]
        return restaurants

    def select_restaurants(self, restaurants, stay_days):
        sorted_restaurants = restaurants.sort_values(by=["rating", "num_reviews"], ascending=False)
        selected_restaurants = sorted_restaurants.head(2 * stay_days).copy()
        trip_days = np.arange(1, stay_days + 1)
        trip_days = np.tile(trip_days, 2)[:2 * stay_days]
        selected_restaurants['trip_day'] = trip_days
        return selected_restaurants
    
    def generate_itinerary(self):
        suggestions = []
        trip_row = self.trip_details.iloc[-1]
        destination_city = trip_row['destination_city']
        destination_country = trip_row['destination_country']
        stay_days = trip_row['stay_days']
        budget_range = trip_row['budget_range']
        activities = trip_row['activities']
        activities_costs = trip_row['activities_costs']
        activities_days = trip_row['activities_days']
        
        attractions = self.get_attractions_for_city(destination_city)
        selected_attractions = self.select_attractions(attractions, stay_days)
        for _, attraction in selected_attractions.iterrows():
            suggestions.append(["Attraction", destination_country, attraction['name'], attraction['location'], attraction['price_range'], attraction['rating'], attraction['trip_day']])

        restaurants = self.get_restaurants_for_city(destination_city, budget_range)
        selected_restaurants = self.select_restaurants(restaurants, stay_days)
        for _, restaurant in selected_restaurants.iterrows():
            suggestions.append(["Restaurant", destination_country, restaurant['name'], restaurant['location'], restaurant['price_range'], restaurant['rating'], restaurant['trip_day']])
        
        suggestions_df = pd.DataFrame(suggestions, columns=["category", "Country", "suggestion", "location", "price_range", "rating", "trip_day"])
        meal_prices_df = pd.read_csv("data/CountrySpecific_RestaurantCost.csv")  
        suggestions_with_costs = pd.merge(suggestions_df, meal_prices_df, on='Country', how='left')
        
        def calculate_estimated_cost(row):
            if row['category'] == 'Restaurant':
                if row['price_range'] == '$$$$$':
                    return row['Price'] * 4  
                if row['price_range'] == '$$$$':
                    return row['Price'] * 3.5  
                if row['price_range'] == '$$$':
                    return row['Price'] * 2.25  
                elif row['price_range'] == '$$':
                    return row['Price'] * 1.5  
                else:
                    return row['Price']
            else:
                if row['price_range'] == '$':
                    return 15  
                elif row['price_range'] == '$$':
                    return 38  
                elif row['price_range'] == '$$$':
                    return 75  
                elif row['price_range'] == '$$$$':
                    return 150
                
        suggestions_with_costs['estimated_cost'] = suggestions_with_costs.apply(calculate_estimated_cost, axis=1)
        suggestions_with_costs = suggestions_with_costs[['trip_day', 'category', 'suggestion', 'location', 'price_range', 'rating', 'estimated_cost']]

        activities_data = {
            'trip_day': activities_days,
            'category': ['custom_activity'] * len(activities),
            'suggestion': activities,
            'location': ['' for _ in activities],
            'price_range': ['' for _ in activities],
            'rating': [None for _ in activities],
            'estimated_cost': activities_costs,
        }

        activities_df = pd.DataFrame(activities_data)
        combined_df = pd.concat([activities_df, suggestions_with_costs])
        sorted_combined_df = combined_df.sort_values(by="trip_day")
        sorted_combined_df.to_csv("itinerary.csv", index=False)
        print(f"\nItinerary saved to itinerary.csv!")

        return sorted_combined_df

