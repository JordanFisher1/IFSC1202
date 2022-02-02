x = int(input("Enter a 3 digit number: "))
hundredsplace = (x//100)
onesplace = (x%10)
tensplace = int(x/10)%10
swappednumber = str(onesplace)+str(tensplace)+str(hundredsplace)
print("Reverse of Digits: {}".format(swappednumber))
