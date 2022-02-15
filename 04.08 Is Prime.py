num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")
elif num == 0 or 1:
    print(num, "is a neither prime NOR composite number")
else:
    print("COMPOSITE")