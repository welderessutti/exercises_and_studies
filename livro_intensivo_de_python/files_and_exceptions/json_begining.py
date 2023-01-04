import json

numbers = [1, 2, 3, 4, 5]

with open("numbers.json", "w") as file_obj:
    json.dump(numbers, file_obj)

with open("numbers.json", "r") as file_obj:
    content = json.load(file_obj)

print(content)
print()


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


def get_stored_username():
    try:
        with open("username.json", "r") as file_obj_01:
            username = json.load(file_obj_01)
    except FileNotFoundError:
        return False
    else:
        return username


def get_new_username():
    username = input("What's your name?: ")
    with open("username.json", "w") as file_obj_02:
        json.dump(username, file_obj_02)
    return username


greet_user()
