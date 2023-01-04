with open("programming.txt", "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open("programming.txt", "a") as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
