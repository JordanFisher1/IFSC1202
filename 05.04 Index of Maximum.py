a = int(input("Enter Number (zero to quit):"))
b =int(input("Enter Number (zero to quit):"))
c = int(input("Enter Number (zero to quit):"))
d = int(input("Enter Number (zero to quit):"))
if (a>b) and (a>c) and (a>d):
    maximum = a
    index = 1
if (b>a) and (b>c) and (b>d):
    maximum = b
    index = 2
if (c>a) and (c>b) and (c>d):
    maximum = c
    index = 3
if (d>a) and (d>b) and (d>c):
    maximum = d
    index = 4
if ( a == 0) and (d == 0) and b == 0 and c == 0:
    maximum = 0
    index = 0
print("maximum:",maximum)
print("Index of maximum:",index)