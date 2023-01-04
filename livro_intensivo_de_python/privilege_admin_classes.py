from user_class import User


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
