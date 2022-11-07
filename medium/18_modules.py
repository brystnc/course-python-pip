import collections
import time
import re
import sys
print(sys.path)

text = 'Mi numero de telefono es 311 123 121, el codigo del pais es 57, mi numero de la suerte 3'
result = re.findall('[0-9]+', text)
print(result)

timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = collections.Counter(numbers)
print(counter)
