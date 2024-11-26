a = True
b = False
c = True
print(a or b)  # True
print(b or c)  # True
print(a or c)  # True
print(b or b)  # False
print(a and b)  # False
print(b and c)  # False
print(a and c)  # True
print(b and b)  # False
x = True
y = False
z = True
print(x or y)   # True
print(y or z)   # True
print(x or z)   # True
print(x or x)   # True
print(x and y)  # False
print(y and z)  # False
print(x and z)  # True
print(x and x)  # True
print((x or y) and z)  # True
print((y or z) and x)  # True
a = 5
b = 10
c = 15
x = True
y = False
print(a < b and x)  # True
print(b > c or y)  # False
print(a == 5 and x)  # True
print(c != b and y)  # False
print(a <= b or x)  # True
print(a > c or (x and y))  # False
print((a + b) > c or x)  # True
print(x and (a < b))  # True
print((b == 10) or (c != 15))  # True
print((x or y) and (a != b))  # True
