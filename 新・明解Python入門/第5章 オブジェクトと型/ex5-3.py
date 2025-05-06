a = 5
b = 7
print((id(a), id(b)))
a, b = b, a
print((id(a), id(b)))
