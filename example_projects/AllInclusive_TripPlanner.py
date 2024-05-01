import webbrowser
from hotel_booking import book_hotel
from budget import budget
from countries_and_cities import countries, my_dict
from flight_booking import book_flight
from welcome_ascii import logo

Factor = 0
user_budget = 0
days = 0

# Logo
print(logo)


# Planning Start
user_name = input("Hello There! What is your Name?\n")
if user_name == "":
    print("Please Enter a valid name and city.")
elif user_name != "":
    print(f"Hello {user_name}, Your city has been set to Mumbai for Best Deals")
    i = 1
    print("Our services extend to various countries! Right now we can offer you a quality "
          "time in one of the following:")
    for country in countries:
        print(f"{i}" + " " + country)
        i += 1
    country_choice = int(input("So, which country are you interested in? Please type in the index number: "))

    # Country Chosen
    my_country = countries[country_choice - 1]
    print(f"{my_country} is an amazing choice indeed! In {my_country} we offer a tour in the following cities: \n")
    i = 1
    for c in my_dict[my_country]:
        print(f"{i}. {c}")
        i += 1
    city_choice = int(input("\n So which city you want to go to enter its index number: "))
    if city_choice > 5:
        print("Please enter the correct index from the list!")
    elif city_choice < 6:
        city = my_dict[my_country][city_choice - 1]
        print(f"So you want to go to {city}, That's an awesome choice!")

        # City Info
        info_city = input(f"Do you want to know more about {city}? (Y/N): ").lower()
        if info_city == "y":
            url_city = "https://en.wikipedia.org/wiki/" + city
            webbrowser.get('windows-default').open_new(url_city)
        elif info_city == "n":
            print(f"It seems you already know about {city}! Awesome")
        nop = int(input("\nPlease tell us the number of people travelling with you, "
                        "So we can plan your trip better: "))
        if nop == 0:
            print("So it is a Solo Trip!")
        else:
            print(f"So {nop} are going together, We hope you have a great time!")
        days = int(input("\nHow many days are you planning to stay? "))
        user_budget = int(input("\nHow much money in INR are you planning to take:"))

        # Budget
        budget(country_choice, my_country, user_budget, days)
        hotel_booked = False
        choice = input("Now let's see the hotel where you will be staying at: Shall we(Y/N)? ").lower()

        # Hotel
        if not hotel_booked:
            if choice == 'y':
                book_hotel(choice, city)
                hotel_booked = True
            else:
                print("We will come back to this step later on.")
        print("\n Now let's Book Flight Tickets.")

        # Flight
        book_flight(city)
        if not hotel_booked:
            choice = input("Now let's see the hotel where you will be staying at: Shall we(Y/N)? ").lower()
            if choice == 'y':
                book_hotel(choice, city)
            else:
                print("Thank You")
        print(f"We genuinely hope you have an amazing trip and return home with plenty \nof unforgettable "
              f"moments!Hope you'"
              f"ll think of us next time when you\nwish to travel once again. See you later, {user_name}")
