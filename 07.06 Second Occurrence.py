s=input("Enter a string: ")
strr=s[:-1]
ind1=s.count("f")
if (ind1<1):
    print('Zero f')
if (ind1>1) and (ind1 != 1):
    ind=strr.find("f")
    ind2 = strr.find("f",ind+1)
    print(ind2)
if (ind1 == 1):
    print("One f")
