with open('./text.txt') as file:
    for line in file:
        print(line)
    file.write('\nCosa nueva')

with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
        file.write('nuevas cosas\n')
        file.write('otra linea\n')
        file.write('otra otra linea\n')

with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)
        file.write('\nnuevas cosas\n')
        file.write('otra linea\n')
        file.write('otra otra linea\n')

with open('./text.txt', 'w') as file:
    for line in file:
        print(line)
        file.write('nuevas cosas')
