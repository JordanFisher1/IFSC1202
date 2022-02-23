from math import pi

def diameter (r):
    d = r*2
    return d

def circumference (r):
    c = 2*r*pi
    return c

def area (r):
    a = pi*r*r
    return a

circlefile = open("06.01 Radius.txt")
radius = circlefile.readline()
print("{:>15s} {:>15s} {:>15s} {:>15s}".format("Radius", "Diameter", "Circumference", "Area"))
while radius != "":
    radiusfp = float(radius)
    print("{:15.5f} {:15.5f} {:15.5f} {:15.5f}".format(radiusfp, diameter(radiusfp), circumference(radiusfp), area(radiusfp)))
    radius = circlefile.readline()
circlefile.close()