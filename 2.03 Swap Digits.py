x = int(input("Enter a two digit number: "))
firstdigit=x//10
seconddigit=x%10
swappednumber = (int(seconddigit*10)+(firstdigit))
print("Swapped Number: {}".format(swappednumber))
