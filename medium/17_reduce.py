import functools

numbers = [8, 2, 3, 5]


def accum(counter, item):
    print('counter: ', counter, 'item', item)
    return counter + item


result = functools.reduce(lambda counter, item: counter + item, numbers)
result = functools.reduce(accum, numbers)
print(result)
