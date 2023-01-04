def show_magicians(magic, great):
    while magicians:
        current_magician = magicians.pop()
        great_magicians.append(f"Great {current_magician}!")
    print(magicians)


def make_great(show):
    for great_magician in great_magicians:
        print(great_magician)


magicians = ["Lewis", "Charles", "Robert", "James"]
great_magicians = []

show_magicians(magicians[:], great_magicians)
make_great(great_magicians)
