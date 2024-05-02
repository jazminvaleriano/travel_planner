# Import the TripPlanner class
from trip_planner import TripPlanner

def test_trip_planner():
    # Create an instance of TripPlanner
    planner = TripPlanner()

    # Simulate planning a trip
    planner.plan_trip()

    # Get the trip details
    trip_details = planner.get_trip_details()
    print("\nTrip Details:")
    print(trip_details)

    # Test selecting attractions
    city = "Paris"  # Example city
    stay_days = 3
    attractions = planner.get_attractions_for_city(city)
    print("\nFiltered Attractions for", city)
    print(attractions)
    selected_attractions = planner.select_attractions(attractions, stay_days)
    print("\nSelected Attractions for", city, "for", stay_days, "days:")
    print(selected_attractions)

    # Get itinerary details 
    planner.generate_itinerary()


if __name__ == "__main__":
    test_trip_planner()
