# Trip Planner
# ------------
# The following program helps to create a travel itinerary


# Import modules
import destinations
import currency


def main():
    # Print a welcome message
    print_welcome()

    # Show destinations
    destinations.print_options()

    # Pick destination
    choice = destinations.get_choice()

    # Get destination info
    destination, euro_rate = destinations.get_info(choice)

    # Calculate currency exchange
    dollar_rate = currency.convert_dollars_to_euros(euro_rate)

    # Determine length of stay
    while True:
        try:
            length_of_stay = int(input(f"And how many days will you be staying in {destination}? "))
            # Check for non-positive input
            if length_of_stay < 0:
                print("Please enter a positive number of days.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            break

    # Calculate cost
    cost = dollar_rate * length_of_stay

    # Save itinerary
    try:
        save_itinerary(destination, length_of_stay, cost)

    # Catch file errors
    except:
        print("Error: the itinerary could not be saved.")

    # Print confirmation
    else:
        print(f"Your trip to {destination} has been booked!")
        print(f"Estimated cost in dollars: ${cost:.2f}")  # Print the estimated cost in dollars




# Function to print a welcome message
def print_welcome():
    # Print a welcome message
    print("---------------------------")
    print("Welcome to the Trip Planner")
    print("---------------------------")


# Function to save the itinerary to a file
def save_itinerary(destination, length_of_stay, cost):
    # Itinerary File Name
    file_name = "itinerary.txt"

    # Open the file in write mode
    with open(file_name, "w") as itinerary_file:
        # Write trip information
        itinerary_file.write("Trip Itinerary\n")
        itinerary_file.write("--------------\n")
        itinerary_file.write(f"Destination: {destination}\n")
        itinerary_file.write(f"Length of stay: {length_of_stay}\n")
        itinerary_file.write(f"Cost: ${cost:,.2f}\n")


# Call main function
main()

