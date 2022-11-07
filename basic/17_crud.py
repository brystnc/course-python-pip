import string
from unicodedata import numeric


numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

# Agrega un elemento al final
numbers.append(700)


# Agrega un elemento al inicio
numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

print(new_list.index('todo 2'))
print(new_list)


new_list.remove('todo 1')
print(new_list)

# Elimina el último elemento
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 4, 5, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

# Error
# new_list.sort()
