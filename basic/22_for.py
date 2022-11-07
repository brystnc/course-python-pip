'''
for element in range(1, 21):
    print(element)
'''
my_list = [23, 45, 67, 89, 43]

for element in my_list:
    print(element)


my_tuple = ('Bryan', 'Stalin')
for element in my_tuple:
    print(element)

product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

# Iteraciones de las llaves
for element in product:
    print(element)

for key in product:
    print(product[key])

for key, value in product.items():
    print(key, '=>', value)


people = [
    {
        'name': 'Bryan',
        'age': 23
    },
    {
        'name': 'José',
        'age': 25
    }
]

for person in people:
    print('name => ', person['name'])
