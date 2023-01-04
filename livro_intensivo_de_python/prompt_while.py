prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your name? "quit" to end the program: '

name = input(prompt)

print(f'Hello {name}!')

message = ''

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue  # FAZ IGNORAR O RESTANTE DO CÓDIGO E VOLTA PARA O INÍCIO DO LAÇO.
    print(current_number)
