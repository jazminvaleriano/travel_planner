from trip_planner import TripPlanner
#from budget_manager import BudgetManager
#from data_visualization import DataVisualizer

def main():
    # Initialize objects
    trip_planner = TripPlanner()
    #budget_manager = BudgetManager()
    #data_visualizer = DataVisualizer()
    
    # Welcome message
    print("---------------------------")
    print("Welcome to TripTrek!")
    print("---------------------------")
    
    # Menu options
    while True:
        print("\nMenu:")
        print("1. Plan Trip")
        print("2. Manage Budget")
        print("3. Visualize Trip Data")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Plan trip
            trip_planner.plan_trip()
            # Generate and display itinerary
            itinerary = trip_planner.generate_itinerary()
    
            # Save itinerary to CSV
            itinerary.to_csv("itinerary.csv", index=False)
    
            print("Itinerary saved to 'itinerary.csv'")
            
        elif choice == '2':
            budget_manager.manage_budget()
        elif choice == '3':
            data_visualizer.visualize_data()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
