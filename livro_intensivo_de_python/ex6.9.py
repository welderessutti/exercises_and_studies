favorite_places = {}
places = {}

name = input("Name: ")
places["First"] = input("First: ")
places["Second"] = input("Second: ")
places["Third"] = input("Third: ")

favorite_places[name] = places.copy()

for k, v in favorite_places.items():
    print(f"{k}'s favorite places are {v['First']}, {v['Second']} and {v['Third']}.")
