print(not True)
print(not False)

# and
print('And operator')
print('not True and True is ', not (True and True))
print('notTrue and False is ', not (True and False))
print('not False and True is ', not (False and True))
print('not False and False is ', not (False and False))

stock = int(input('Ingrese el invetario: '))
print(not (stock >= 100 and stock <= 1000))
