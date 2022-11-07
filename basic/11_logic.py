# and
print('And operator')
print('True and True is ', True and True)
print('True and False is ', True and False)
print('False and True is ', False and True)
print('False and False is ', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

stock = int(input('Ingrese el invetario: '))
print(stock >= 100 and stock <= 1000)

# or
print('Or operator')
print('True or True is ', True or True)
print('True or False is ', True or False)
print('False or True is ', False or True)
print('False or False is ', False or False)

role = input('Digita tu rol: ')
print(role == 'admin' or role == 'seller')
