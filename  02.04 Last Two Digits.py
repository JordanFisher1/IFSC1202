x = int(input("Enter a number: "))
onesplace = x%10
tensplace = int(x/50)
hundredsplace = 
lasttwodigits = (str(tensplace)+ str(onesplace))
print ("Last Two digits: {}".format(lasttwodigits))