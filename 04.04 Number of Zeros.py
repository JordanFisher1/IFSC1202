N = int(input("Enter N: "))
sum = 0
for N in range(1, N+1):
    x = (int(input("Enter Number: "))) 
    if (x == 0):
        sum = (sum + 1)
print("Number of zeros: ",sum)