
import random


def choose_options():
    user_option = input('Piedra, papel o tijera: ').lower()

    # Tupla
    options = ('piedra', 'papel', 'tijera')
    computer_option = random.choice(options)

    print(f'Your option is {user_option}')
    print(f'Computer option is {computer_option}')

    if not user_option in options:
        print('Opción no válida')
        return None, None

    return user_option, computer_option


def check_rules(user_option, computer_option, rounds_win_user, rounds_win_computer):
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
    return rounds_win_user, rounds_win_computer


def check_winner(rounds_win_user, rounds_win_computer):
    print(f'Rounds win of User {rounds_win_user}')
    print(f'Rounds win of Computer {rounds_win_computer}')


def run_game():
    number_round = 1
    rounds_win_user = 0
    rounds_win_computer = 0
    while not (rounds_win_computer > 1 or rounds_win_user > 1):
        print('*' * 5)
        print('Round', number_round)
        print('*' * 5)

        user_option, computer_option = choose_options()
        rounds_win_user, rounds_win_computer = check_rules(
            user_option, computer_option, rounds_win_user, rounds_win_computer)
        check_winner(rounds_win_user, rounds_win_computer)
        number_round += 1


run_game()
