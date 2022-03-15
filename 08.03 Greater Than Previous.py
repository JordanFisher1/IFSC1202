a = [int(s) for s in input("Enter Values Seperated by Spaces:").split()]
for i in a[1:]:
    if i > a[a.index(i)-1]:
        print(i," ", end="")