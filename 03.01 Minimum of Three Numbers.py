x = (input("Enter first number: "))
y = (input("Enter second number: "))
z = (input("Enter third number: "))
if x<y and x<z:
    smallest = x
if y<x and y<z:
    smallest = y
if z<x and z<y:
    smallest = z
print(smallest)

