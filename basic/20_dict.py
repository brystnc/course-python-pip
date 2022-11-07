person = {
    'name': 'Bryan',
    'last_name': 'Carvajal',
    'lang': ['python', 'js'],
    'age': 99
}

print(person)

person['name'] = 'Stalin'
person['age'] -= 50
person['lang'].append('rust')
print(person)

del person['last_name']
person.pop('age')

print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
