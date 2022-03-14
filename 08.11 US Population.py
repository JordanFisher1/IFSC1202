listpopulation = []
listchange=[0]
listpercent = [0]
file = open("08.11 USPopulation.txt", "r")
for i in file:
    listpopulation.append(int(i)*1000)
file.close()
for i in range(41):
    if(i>=1):
        change = listpopulation[i]-listpopulation[i-1]
        listchange.append(change)
        percentchange = round(((change)/(listpopulation[i-1]))*100,2)
        listpercent.append(percentchange)
j=0
print("Year\t\tPopulation\t\tChange\t\tPercent Change")
for year in range(1950,1991):
    if(j==0):
        print(year,"\t\t",listpopulation[j],"\t\t","N/A","\t\t","N/A")
    else:
        print(year,"\t\t",listpopulation[j],"\t\t",listchange[j],"\t",str(listpercent[j])+"%")
    j+=1
average = sum(listchange)/41
print("Average population change:",change)
maxi = listchange[1]
mini = listchange[1]
maxindex = 0
minindex = 0
for i in range(2,len(listchange)):
    if(listchange[i]>maxi):
        maxi = listchange[i]
        maxindex = i
    if(listchange[i]<mini):
        mini=listchange[i]
        minindex=i
print("Minimum change and year:",mini,1950+minindex)
print("Maximum change and year:",maxi,1950+maxindex)