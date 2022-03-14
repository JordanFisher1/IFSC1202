inputlist = list()
a = input("Enter values seperated by spaces: ").split()
n = len(a)
for i in range(n):
    inputlist.append(int(a[i]))
for i in range(n):
    count = 1
    for j in range(n):
        if inputlist[i] == inputlist[j] and i != j:
            count += 1
    if count == 1:
        print(inputlist[i], end = " ")