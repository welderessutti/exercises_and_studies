cities = {}

while True:
    city = input("City: ")
    cities[city] = {"Country": input("Country: "), "Population": input("Population: "),
    "Facts": input("Facts: ")}

    keep = input("Continue?: ").strip().upper()

    if keep == "N":
        break

for k, v in cities.items():
    print(f"{k} is a city of {v['Country']}. Its population is about {v['Population']}. A curiosity about this city is {v['Facts']}.")
