FileA = open("06.05 CompareFileA.txt")
FileB = open("06.05 CompareFileB.txt")
lst1 = []
lst2 = []
for l in FileA:
    lst1.append(l)
for l in FileB:
    lst2.append(l)
count = 2
for i in range(len(lst1)):
    if (lst1[i] != lst2[i]):
        print(f"Line :{i+1} - {lst1[i]}")
        print(f"Line :{i+1} - {lst2[i]}")
print(count, "differences")
FileA.close()
FileB.close()