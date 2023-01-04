people = []
person = {}

while True:
    person["First name"] = input("Name: ")
    person["Last name"] = input("Last name: ")

    people.append(person.copy())

    keep = input("Deseja continuar?: ").strip().upper()
    if keep == "N":
        break

for i, v in enumerate(people):
    print(f"The {i + 1}º person's name is: {v['First name']} {v['Last name']}")

# OUTRA FORMA DE INCLUIR UM DICIONÁRIO DENTRO DE UMA LISTA:
'''people = []

people.append({"First name": input("name: "), "Last name": input("last: ")})

print(people)'''
