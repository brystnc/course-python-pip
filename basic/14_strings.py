from ctypes import sizeof


text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien')
else:
    print('Mala suerte')

size = len('amor ')
print(size)

print(text)
print(text.upper())
print(text.lower())
# ¿Cuántas 'a' hay en 'text'?
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Python'))
print(text.replace('Python', 'Change'))

text_2 = 'este es un titulo'
print(text)
# Coloca en mayúsucla la primera letra
print(text_2.capitalize())
# Coloca en mayúsculas las primeras letras
print(text_2.title())
print(text_2.isdigit())