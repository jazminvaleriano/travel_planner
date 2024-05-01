import webbrowser


def book_hotel(user_choice, user_city):
    if user_choice == "y":
        url_h_dict = {}
        with open("cities_trip_adviser.txt") as f:
            for line in f:
                key, value = line.split()

                url_h_dict[key] = value
            url_hotel = f"https://www.tripadvisor.in/{url_h_dict[user_city]}.html"
            webbrowser.get("windows-default").open_new(url_hotel)
            hotel_booked = True
        return hotel_booked
