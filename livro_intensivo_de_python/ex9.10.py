from restaurant_icecream_classes import Restaurant, IceCreamStand

lista = ["Chocolate", "Pistache", "Morango", "Creme"]
sorveteria = IceCreamStand("Fruity", "Doces", lista)

print(sorveteria.show_flavors())

print(f"The ice creams flavors are: ", end="")
for flavor in range(len(sorveteria.flavors)):
    if flavor != len(sorveteria.flavors) - 1:
        print(sorveteria.flavors[flavor], end=", ")
    else:
        print(sorveteria.flavors[flavor], end=".")
