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


class Admin(User):
    def __init__(self, first, last, age, height, weight):
        super().__init__(first, last, age, height, weight)
        self.privileges = Privileges()

    def __getitem__(self, item):
        return self.privileges.privileges[item]


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        return self.privileges


administrador = Admin("Welder", "Ressutti", 34, 1.80, 92)

print(administrador.privileges.show_privileges())

print(f"The admin privileges are: ", end="")
for privilege in range(len(administrador.privileges.privileges)):
    if privilege != len(administrador.privileges.privileges) - 1:
        print(administrador.privileges.privileges[privilege], end=", ")
    else:
        print(administrador.privileges.privileges[privilege], end=".")
