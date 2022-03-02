s=input("Enter a string: ")
strr=s[::-1]
ind1=s.find("f")
if (ind1 == -1):
    print(0)
else:
    ind=strr.find("f")
    n=len(s)
    ind2=n-ind-1
    if ind1 == ind2:
        print(ind1)
    else:
        print(ind1,ind2)