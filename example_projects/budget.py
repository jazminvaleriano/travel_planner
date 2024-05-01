Factor = 0


def budget(country_choice, chosen_country, user_money, day_specified):
    global Factor
    if country_choice == 1:
        Factor = 0.55
    elif country_choice == 2:
        Factor = 0.67
    elif country_choice == 3:
        Factor = 0.86
    elif country_choice == 4:
        Factor = 0.92
    elif country_choice == 5:
        Factor = 0.86

    print(f"{user_money} INR is around {int(user_money*Factor)} in {chosen_country}'s Native Currency.")
    if user_money < 9000:
        print("\nEntered, Amount is not sufficient for you to enjoy the trip.")
    else:
        print("\nThis much money is more than enough for you to enjoy this trip to the fullest!")
        print(f"\nThis much money is sufficient! You'll spend around"
              f" {int((user_money * Factor) / day_specified)} per person on Average.")
