x = int(input(" Enter Length of Race in Kilometers: "))
y = int(input(" Enter Minutes: "))
z = int(input(" Enter Seconds: "))
a = (x / 1.61)
b = (y / 60)
c = (z / 60) / 60
totalhours = (b + c)
print (a / totalhours)