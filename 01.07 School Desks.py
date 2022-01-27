x = input("Enter Classroom A: ")
y = input("Enter Classroom B: ")
z = input("Enter Classroom C: ")
a = int(x) 
b = int(y) 
c = int(z) 
remainder = (a + b + c) % 2
total = (a + b + c) / 2
print (int(total + remainder))