class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}.")
        print(f"Its cuisine type is: {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open!")

    def customers_served(self):
        print(f"The number of customers served was: {self.number_served}.")

    def set_number_served(self, number):
        self.number_served = number


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine, flavors):
        super().__init__(name, cuisine)
        self.flavors = flavors

    def __getitem__(self, item):
        return self.flavors[item]

    def show_flavors(self):
        return self.flavors


lista = ["Chocolate", "Pistache", "Morango", "Creme"]
sorveteria = IceCreamStand("Fruity", "Doces", lista)

print(sorveteria.show_flavors())

print(f"The ice creams flavors are: ", end="")
for flavor in range(len(sorveteria.flavors)):
    if flavor != len(sorveteria.flavors) - 1:
        print(sorveteria.flavors[flavor], end=", ")
    else:
        print(sorveteria.flavors[flavor], end=".")
