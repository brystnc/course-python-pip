
import random

# Tupla
options = ('piedra', 'papel', 'tijera')
computer_option = random.choice(options)


number_round = 1
rounds_win_user = 0
rounds_win_computer = 0

while not (rounds_win_computer > 1 or rounds_win_user > 1):
    print('*' * 5)
    print('Round', number_round)
    print('*' * 5)

    user_option = input('Piedra, papel o tijera: ').lower()

    print(f'Your option is {user_option}')
    print(f'Computer option is {computer_option}')

    if not user_option in options:
        print('Opción no válida')
    if user_option == computer_option:
        print('¡Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User gano')
            rounds_win_user += 1
        else:
            print('Papel gana a piedra')
            print('Computer gano')
            rounds_win_computer += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gano')
            rounds_win_user += 1
        else:
            print('Tijera gana a papel')
            print('Computer gano')
            rounds_win_computer += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('User gano')
            rounds_win_user += 1
        else:
            print('Piedra gana a tijera')
            print('Computer gana')
            rounds_win_computer += 1

    print(f'Rounds win of User {rounds_win_user}')
    print(f'Rounds win of Computer {rounds_win_computer}')
    number_round += 1
