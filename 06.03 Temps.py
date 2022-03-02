def Celsius (f):
    FahrToCel = (f-32)*5/9
    return FahrToCel
count = 0
tempfile = open("06.03 FTemps.txt")
celsiusfile = open("06.03 CTemps.txt", "w")
x = tempfile.readline()
while x != "":
    count += 1
    y = float(x)
#    print("{:>5.1f}".format(y))
    celsiusfile.write("{:5.1f}".format(Celsius(y)) + "\n")
    x = tempfile.readline()
tempfile.close()
celsiusfile.close()
print(count, "records written")
