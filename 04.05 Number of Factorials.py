N = int(input("Enter Number: "))
sum = 0
for i in range(0,N): 
    product = 1
    for j in range(1,i+1):
        product = (product * j)
    sum = (sum + product)
print(sum)