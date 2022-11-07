items = [
    {
        'product': 'camosa',
        'price': 300,
    },
    {
        'product': 'medos',
        'price': 300
    },
    {
        'product': 'pantalones_v2',
        'price': 200
    }
]

prices = list(map(lambda item: item['price'], items))
print(prices)

'''
def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item


new_items = list(map(add_taxes, items))
print(new_items)
print(items)
'''


def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item


new_items = list(map(add_taxes, items))
print(new_items)
print(items)
