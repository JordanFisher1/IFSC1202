x = int(input("Enter a three digit number: "))
hundredsplace = int(x/100) 
tensplace = int(x/10)%10
onesplace = (x%10)
if hundredsplace<tensplace<onesplace:
    print("YES")
else:
    print("NO")