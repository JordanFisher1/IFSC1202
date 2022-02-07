x = int(input("Enter Point A: "))
y = int(input("Enter Point B: "))
z = int(input("Enter Point C: "))
if x<y<z:
    distance = (y-x)
if y<x<z:
    distance = (x-y)
if x<z<y:
    distance = (z-x)
if z<x<y:
    distance = (x-z)
if z<y<x:
    distance = (x-y)
if y<z<x:
    distance = (x-z)
print (distance)