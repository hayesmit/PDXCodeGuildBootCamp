#lab09-Unit_Converter.py

distance = float(input("what distance in do you want to convert to meters? example 167 >> "))
currentUnits = input("what is the current unit of measurement, ft, mi, m, km, yd, in?")
finalUnits = input("What units would you like the result to be in? in, ft, yd, m, mi, km? >> ")

if currentUnits == "ft":
    conversion = distance * .3048
elif currentUnits == "mi":
    conversion = distance * 1609.34
elif currentUnits =="m":
    conversion = distance
elif currentUnits == "km":
    conversion = distance * 1000
elif currentUnits == "yd":
    conversion = distance * 0.9144
elif currentUnits == "in":
    conversion = distance * 0.0254

if finalUnits == "ft":
    conversion /= .3048
elif finalUnits == "mi":
    conversion /= 1609.34
elif finalUnits == "km":
    conversion /= 1000
elif finalUnits == "yd":
    conversion /= 0.9144
elif finalUnits == "in":
    conversion /= 0.0254

print(str(distance) + currentUnits + " equals " + str(conversion) + finalUnits)
