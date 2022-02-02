x = int(input("Enter a three digit number: "))
hundredsplace = int(x/100) 
tensplace = int(x/10)%10
onesplace = (x%10)
sumofdigits = hundredsplace + tensplace + onesplace
print (" Sum of digits: {}".format(sumofdigits))