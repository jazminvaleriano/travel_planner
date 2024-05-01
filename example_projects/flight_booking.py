import webbrowser

code_dict = {}


with open("cleartrip.txt") as f:
    for line in f:
        key, value = line.split()

        code_dict[key] = value


def book_flight(city):
    url = ""
    city_code = code_dict[city]
    print("\nWhich of the following sites do you prefer")
    site = int(input("1.Clear Trip\n2.Goibibo\n3.Yatra.com\nChoice: "))
    if site == 1:
        url = f"https://www.cleartrip.com/flights/international/results?" \
              f"from=BOM&to={city_code}&depart_date=29/04/2021&adults=1&childs=0&infants=0&class=" \
              f"Economy&airline=&carrier=&intl=y&sd=1524084890374&page=loaded"
    elif site == 2:
        url = f"https://www.goibibo.com/flights/air-BOM-{city_code}-20210429-20210505-1-0-0-E-I/"
    elif site == 3:
        url = f"https://www.yatra.com/international-flights/mumbai-to-{city}-flights"
    info2 = input("Proceed to Website? (Y/N): ").lower()
    if info2 == "y":
        webbrowser.get("windows-default").open_new(url)
        book = input("Did you find your desired seat?(Y/N): ").lower()
        if book == "n":
            book_flight(city)
        else:
            print("\n Ok that's Great!")
    else:
        print("Ok, we'll do that later")
        book_flight(city)
