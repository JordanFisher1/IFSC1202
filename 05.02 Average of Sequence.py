n=int(input("Enter the number of non zero numbers: "))
a=[]
for i in range(1,n+1):
    elem=int(input("Enter the numbers: "))
    a.append(elem)
    avg=sum(a)/n
if (n == 0):
    avg = 0
print(avg)
