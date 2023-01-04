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


class User:
    def __init__(self, first, last, age, height, weight):
        self.first_name = first
        self.last_name = last
        self.full_name = f"{self.first_name} {self.last_name}"
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        print(f"The user's full name is: {self.full_name}.")
        print(f"Its age is: {self.age} years old, its height is: {self.height} m and its weight is: {self.weight} kg.")

    def greet_user(self):
        print(f"Nice to meet you {self.full_name}!")

    def get_login_attempts(self):
        print(f"The user {self.full_name} tried {self.login_attempts} login attempts.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


restaurant = Restaurant("Tia Joana", "Caseira")

restaurant.customers_served()
restaurant.set_number_served(15)
restaurant.customers_served()

user = User("Welder", "Ressutti", 34, 1.80, 92)

print()
user.get_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
user.reset_login_attempts()
user.get_login_attempts()
