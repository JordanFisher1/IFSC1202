x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x == y:
    index = ("3")
if y == x:
    index = ("3")
if x == z:
    index = ("2")
if z == x:
    index = ("2")
if y == z:
    index = ("1")
if z == y:
    index = ("1")
print(index)
