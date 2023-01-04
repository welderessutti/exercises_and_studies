def build_person(first_name, last_name, age=0):
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("Jimmy", "Hendrix", 27)
print(musician)


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name


while True:
    print(f"\nPlease tell me your name: ")
    f_name = input("First name: ")
    if f_name == "q":
        break
    l_name = input("Last name: ")
    if l_name == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name.title()}!")
