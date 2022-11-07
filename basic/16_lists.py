'''
1. Puede ser modificada
2. Cada elemento esta separado por una coma
3. Puede contener todo tipo de datos
'''

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

# Strings no mutable
text = 'Hola'
#text[0] = 'm'

tasks[0] = 'Watch platzi courses'
print(tasks)
print(numbers[0:3])
print(True in types)
