with open("learning_python.txt", "r") as file_object:
    content = file_object.read()
print(content)
print()

with open("learning_python.txt", "r") as file_object:
    for line in file_object:
        print(line.strip())
print()

with open("learning_python.txt", "r") as file_object:
    contents_lines = file_object.readlines()
for line in contents_lines:
    print(line.strip())
print()

file_strings = ""
for line in contents_lines:
    file_strings += line.strip() + "\n"
print(file_strings)

file_strings_01 = ""
for line in contents_lines:
    file_strings_01 += line.strip().replace("Python", "C") + "\n"
print(file_strings_01)
