FromValue = (float(input("Enter From Value: ")))
FromUnit = input("Enter From Unit (in, ft, yd, mi): ")
ToUnit = input("Enter To Unit (in, ft, yd, mi): ")
if (FromUnit == "in") and (ToUnit == "ft"):
    ToValue = (round(FromValue/12,7))
if (FromUnit == "in") and (ToUnit == "yd"):
    ToValue = (round(FromValue/36,7))
if (FromUnit == "in") and (ToUnit == "mi"):
    ToValue = (round(FromValue/63360,7))
if (FromUnit == "ft") and (ToUnit == "in"):
    ToValue = (round(FromValue*12,7))
if (FromUnit == "ft") and (ToUnit == "yd"):
    ToValue = (round(FromValue/3,7))
if (FromUnit == "ft") and (ToUnit == "mi"):
    ToValue = (round(FromValue/5280,7))
if (FromUnit == "yd") and (ToUnit == "in"):
    ToValue = (round(FromValue*36,7))
if (FromUnit == "yd") and (ToUnit == "ft"):
    ToValue = (round(FromValue*3,7))
if (FromUnit == "yd") and (ToUnit == "mi"):
    ToValue = (round(FromValue/1760,7))
if (FromUnit == "mi") and (ToUnit == "in"):
    ToValue = (round(FromValue*63360,7)) 
if (FromUnit == "mi") and (ToUnit == "ft"):
    ToValue = (round(FromValue*5280,7))
if (FromUnit == "mi") and (ToUnit == "yd"):
    ToValue = (round(FromValue*1760,7))
if (FromUnit == "in") and (ToUnit == "in"):
    ToValue = (FromValue)
if (FromUnit == "ft") and (ToUnit == "ft"):
    ToValue = (FromValue)
if (FromUnit == "yd") and (ToUnit == "yd"):
    ToValue = (FromValue)
if (FromUnit == "mi") and (ToUnit == "mi"):
    ToValue = (FromValue)
print(FromValue, FromUnit, "=>", ToValue, ToUnit )
