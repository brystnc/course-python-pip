'''
Tuplas
Estructura de datos inmutables que 
contiene una secuencia ordenada de 
elementos
'''
numbers = (1, 2, 3, 5)
strings = ('Nico', 'Zule', 'Santi', 'Nico')
print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])

print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# Error: numbers.append(10)
# numbers[1] = 'change'

print(strings)
print(strings.index('Zule'))
print(strings.count('Nico'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'julo'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
