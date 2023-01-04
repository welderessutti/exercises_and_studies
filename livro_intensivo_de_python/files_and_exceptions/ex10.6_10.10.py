n1 = input("Digit a number: ")
n2 = input("Digit another number: ")

try:
    total = int(n1) + int(n2)
except ValueError:
    print("Invalid type. Only numbers!")
else:
    print(total)
print()

while True:
    try:
        n1 = int(input("Number: "))
        n2 = int(input("Number 2: "))
    except ValueError:
        print("Invalid type. Only numbers!")
    else:
        if n1 == 999 or n2 == 999:
            break
        print(n1 + n2)
print()

with open("dogs.txt", "w") as file_object:
    file_object.write("Phoebe")

try:
    with open("dogs.txt", "r") as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("This file doesn´t exist!")
else:
    print(contents)
try:
    with open("cats.txt", "r") as file_object:
        contents_02 = file_object.read()
except FileNotFoundError:
    print("This file doesn´t exist!")
else:
    print(contents_02)
