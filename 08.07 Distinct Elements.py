a = input("Enter values seperated by spaces: ")
b = a.split()
distinct = len(set(b))
print("Number of Distinct elements: ", distinct)