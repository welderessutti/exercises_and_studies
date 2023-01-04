with open("pi_digits.txt", "r") as file_object:
    contents = file_object.read()
print(contents.strip())
print()

with open("pi_digits.txt", "r") as file_object_01:
    for line in file_object_01:
        print(line.strip())
print()

with open("pi_digits.txt", "r") as file_object_02:
    lines = file_object_02.readlines()
for line in lines:
    print(line.strip())
print()

pi_string = ""
with open("pi_digits.txt", "r") as file_object_03:
    for line in file_object_03:
        pi_string += line.strip()
print(pi_string)
print(len(pi_string))
