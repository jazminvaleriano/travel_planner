import pandas as pd

class TripPlanner:
    def __init__(self):
        self.trip_details = pd.DataFrame(columns=["destination", "start_date", "end_date", "transportation", "accommodation", "activities"])

    def plan_trip(self):
        print("\nTrip Planner:")
        destination = input("Enter destination: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        transportation = input("Enter transportation details: ")
        accommodation = input("Enter accommodation details: ")
        
        activities = []
        while True:
            activity = input("Enter an activity or point of interest (or leave blank to finish): ")
            if not activity:
                break
            activities.append(activity)
        
        trip_data = pd.DataFrame([[destination, start_date, end_date, transportation, accommodation, activities]], 
                                 columns=["destination", "start_date", "end_date", "transportation", "accommodation", "activities"])
        self.trip_details = pd.concat([self.trip_details, trip_data], ignore_index=True)
        print("Trip details saved successfully!")
        
    def get_trip_details(self):
        print(self.get_trip_details)
        return self.trip_details
    
