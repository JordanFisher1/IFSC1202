def isEven (n):
    return (n%2==0)
def isOdd (n):
    return (n%2)
def isPrime (n):
    if (n > 1):
        for i in range (2,n//2):
            if (n%i==0):
                return False
        else:
            return True
    else:
        return False
numbersfile = open("06.06 Numbers.txt", "r")
evennumbersfile = open("6.6 Evennumbers.txt", "w")
oddnumbersfile = open("6.6 Oddnumbers.txt", "w")
primenumbersfile = open("6.6 Primenumbers.txt", "w")
nums = numbersfile.readlines()
evencount = 0
oddcount = 0
primecount = 0
readcount = 0
for line in nums:
    n = int(line.strip())
    if (isEven(n)):
        evennumbersfile.write(str(n)+"\n")
        evencount += 1
    elif (isOdd(n)):
        oddnumbersfile.write(str(n)+ "\n")
        oddcount += 1
    if (isPrime(n)):
        primenumbersfile.write(str(n)+ "\n")
        primecount += 1
    readcount += 1
print("{} even numbers".format(evencount))
print("{} odd numbers".format(oddcount))
print("{} prime numbers".format(primecount))
print("{} read numbers".format(readcount))
numbersfile.close()
evennumbersfile.close()
oddnumbersfile.close()
primenumbersfile.close()

         