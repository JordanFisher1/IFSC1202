Month = (int(input("Enter Month: ")))
y = int(input("Enter Day: "))
if int(0<y<31):
    NextDay = (y+1)
    NextMonth = (Month)
if int(Month<12) and (y == 31):
    NextDay = (1)
    NextMonth = (Month+1)
if int(Month == 12) and (y == 31):
    NextDay = (1)
    NextMonth = (1)
if int(Month == 2) and (y == 28):
    NextDay = (1)
    NextMonth = (3)
print("Next Day:",NextMonth,"/",NextDay)




