x = int(input("Enter a number: "))
onesplace = x%10
tensplace = int(x/10)%10
hundredsplace =  x%1
lasttwodigits = (str(hundredsplace) + (str(tensplace)+ str(onesplace)))
print ("Last Two digits: {}".format(lasttwodigits))