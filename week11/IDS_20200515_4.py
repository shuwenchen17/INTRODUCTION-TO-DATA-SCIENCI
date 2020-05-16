x = 0.25
print(type(x))
print(x.as_integer_ratio())
print(type(x.as_integer_ratio()))

numerator, denominator = x.as_integer_ratio()
print(numerator)
print(denominator)