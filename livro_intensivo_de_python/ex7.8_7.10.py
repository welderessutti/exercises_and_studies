sandwich_orders = ['Atum', 'Picanha', 'Presunto', 'Calabresa', 'Bacon']
finished_sandwiches = []

while sandwich_orders:
    sandwich_prepared = sandwich_orders.pop()
    print(f'I made your {sandwich_prepared} sandwich.')
    finished_sandwiches.append(sandwich_prepared)

print(finished_sandwiches)

print()

sandwich_orders = ['Atum', 'Pastrami', 'Picanha', 'Pastrami', 'Presunto', 'Pastrami', 'Calabresa', 'Bacon']

print(sandwich_orders)

print('We are out of "PASTRAMI SANDWICH".')

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)

print()

responses = {}
polling_active = True

while polling_active:
    name = input("What's your name?: ")
    response = input("If you could visit one place in the world, where would you go?")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no): ")
    if repeat == 'no':
        polling_active = False

for name, response in responses.items():
    print(f'{name} would like to visit {response}.')

print(responses)
