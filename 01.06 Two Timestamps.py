print ("First Timestamp")
a = input ("Enter Hours: ")
b = input ("Enter Minutes: ")
c = input("Enter Seconds: ")
print("Second Timestamp")
d = input("Enter Hours: ")
e = input(" Enter Hours: ")
f = input("Enter Seconds: ")
firsthours = int(a)
firstminutes = int(b)
firstseconds = int(c)
secondhours = int(d)
secondminutes = int(e)
secondseconds = int(f)
totalhours = ((secondhours - firsthours) * 60) * 60
totalminutes = (secondminutes - firstminutes) * 60
totalseconds = (secondseconds - firstseconds)
total = totalhours + totalminutes + totalseconds
print(total)