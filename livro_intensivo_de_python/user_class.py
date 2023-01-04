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
