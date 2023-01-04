poll = {}
people = []

while True:
    name = input("Name: ").strip().title()
    language = input("Language: ").strip().title()

    poll[name] = language

    user_opt = input("Do you want to continue?: ").strip().upper()

    if user_opt == "N":
        break


for k in people:
    if k in poll.keys():
        print(f"Great {k}! Thank you for participating in the survey.")
    else:
        print(f"Hey {k}, let's participate in the survey!")

for v in set(poll.values()):
    print(v)

poll_1 = []

while True:
    person = {"welder": "Ressutti"}

    poll_1.append(person)

    user_opt = input("Do you want to continue?: ").strip().upper()

    if user_opt == "N":
        break

print(poll_1)
