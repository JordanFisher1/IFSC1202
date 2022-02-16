count = int(input("Enter how many numbers there are: "))
nums = []
for i in range(count):
    nums.append(int(input("Enter a number (zero to quit): ")))
    
largest = nums[0]
for i in range(1, len(nums)): 
    if nums[i] > largest: 
        largest = nums[i]
        
print("maximum :", largest)


