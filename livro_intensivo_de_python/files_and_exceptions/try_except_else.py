try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")

    if second_number == "q":
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can´t divide by zero!")
    else:
        print(answer)
print()


def count_words(filename):
    try:
        with open(filename, "r") as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn´t exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


file_list = ["answer.txt", "guest.txt", "learning_python.txt", "alice.txt", "pi_digits.txt", "programming.txt"]

for file in file_list:
    count_words(file)
