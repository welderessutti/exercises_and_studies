class Restaurant:
    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.restaurant_name}.")
        print(f"Its cuisine type is: {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The {self.restaurant_name} is open!")


class User:
    def __init__(self, first, last, age, height, weight):
        self.first_name = first
        self.last_name = last
        self.full_name = self.first_name + " " + self.last_name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        print(f"The user's full name is: {self.full_name}.")
        print(f"Its age is: {self.age} years old, its height is: {self.height} m and its weight is: {self.weight} kg.")

    def greet_user(self):
        print(f"Nice to meet you {self.full_name}!")


restaurant_1 = Restaurant("Daisho", "Japanese")
restaurant_2 = Restaurant("Caipirão", "Caseira")
restaurant_3 = Restaurant("Lima", "Self-Service")

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()

user_1 = User("Welder", "Ressutti", 34, 1.80, 92)
user_2 = User("Carmen", "Bigatti", 63, 1.70, 78)
user_3 = User("Wilnir", "Ressutti", 66, 1.82, 100)

print()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
