x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y)

# To compare we have two forms
# Throught string or mathematic

y_str = format(y, ".2g")
print(y_str)
print(y_str == str(x))

print('*' * 10)

print(y, x)
tolerance = 0.00001
print(x-y)
print(abs(x - y) < tolerance)
