while True:
    guest_name = input("What's your name ('q' to quit)?: ").strip()

    if guest_name == "q":
        break
    else:
        print(f"Welcome {guest_name}!")
        with open("guest.txt", "a") as file_object:
            file_object.write(guest_name + "\n")

while True:
    question = input("Why do you like programming ('q' to quit)?: ")

    if question == "q":
        break
    else:
        with open("answer.txt", "a") as file_object:
            file_object.write(question + "\n")
