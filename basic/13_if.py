if True:
    print('Se ejecutó')

if False:
    print('No se ejecutó')


pet = input('¿Cuál es tu mascota?: ')

if pet == 'perro':
    print('Genial. Tienes un perro')
elif pet == 'gato':
    print('Genial. Tienes un gato')
else:
    print('No tienes una mascota interesante')


stock = int(input('Digita el stock: '))

if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')

number = int(input('Digita el número: '))
if number % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')
