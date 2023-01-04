def show_toppings(*toppings):
    print(f"Making a sandwich with toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print()


show_toppings("Cheese", "Salad", "Tomato")
show_toppings("Onion", "Barbecue Sauce")


def build_user(first, last, **user_info):
    profile = dict()
    profile["First name"] = first
    profile["Last name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_information = build_user("Welder", "Ressutti", Age=34, Location="Indaiatuba", Height="1,80 m", Weight="82 Kg")
print(user_information)
