def city_country(city, country):
    print(f"{city}, {country}")


city_country("London", "United Kingdom")
city_country("Paris", "France")
city_country("Roma", "Italy")


def make_album(artist, album_title, tracks=0):
    musical_album = {"Artist": artist, "Album": album_title, "Tracks": tracks}
    return musical_album


print(make_album("Avenged Sevenfold", "Nightmare", 10))
print(make_album("Oasis", "(What's the Story) Morning Glory?", 12))
print(make_album("Daft Punk", "Random Access Memories", 14))


def make_album(artist, album):
    users = {"Artist": artist, "Album": album}
    return users


while True:
    print("\nPlease, tell me your artist and album name.")
    artist_name = input("Artist name: ").title()
    if artist_name in 'qQ':
        break
    album_name = input("Album name: ").title()
    if album_name in 'qQ':
        break

    user_choice = make_album(artist_name, album_name)

    print(f"\nGood choice! {user_choice}.")
