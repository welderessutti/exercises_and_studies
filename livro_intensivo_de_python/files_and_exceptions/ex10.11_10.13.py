import json

while True:
    try:
        num = int(input("What's your favorite number?: ").strip())
    except ValueError:
        print("Invalid type. Only numbers!")
    else:
        with open("favorite_number.json", "w") as file_obj:
            json.dump(num, file_obj)
        if num:
            break

with open("favorite_number.json", "r") as file_obj:
    content = json.load(file_obj)

print(f"I know what's your favorite number! It's: {content}.")
print()


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
        answer = input("Is your name correct (y or n)?: ")
        if answer == "n":
            username = get_new_username()
            print(f"Sorry! We'll remember your correct name when you come back, {username}!")
        else:
            print(f"Have a good day, {username}!")
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
