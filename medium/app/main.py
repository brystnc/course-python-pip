import utils

keys, values = utils.get_population()
print(keys, values)
print(utils.A)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Venezuela',
        'Population': 300
    },
]

result = utils.population_by_country(data, 'Colombia')
print(result)
