from turtle import width


def find_volume(length=1, width=1, depth=2):
    return length * width * depth, width, 'hola'


result = find_volume(20, depth=3)
result, width, text = find_volume(20, depth=3)
# print(result[0])
