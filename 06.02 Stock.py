def Change (tp,yp):
    percentchange = (tp-yp)/yp*100
    return percentchange  
stockfile = open("6.02 Stock.txt")
print("{:>10s} {:>10s}".format("Price", "Change"))
p = stockfile.readline()
p=float(p)
print("{:>10.2f}".format(p))
yesterday = float(p)

p = stockfile.readline()
while p != "":
    p = float(p)
    change = Change(p,yesterday)
    print("{:>10.2f} {:>10.2f} %".format(p,change))
    yesterday = p
    p = stockfile.readline()
stockfile.close()