x = int(input("Enter a four digit number: "))
thousandsplace = int(x/1000)
hundredsplace = int(x/100)%10
tensplace = int(x/10)%10
onesplace = (x%10)
if thousandsplace == onesplace and hundredsplace == tensplace:
    print ("YES")
else:
    print ("NO")