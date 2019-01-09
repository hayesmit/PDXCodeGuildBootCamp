#lab8-Make_Change.py

amount = input("How much much money do you have, lets make some change? example $4.25  >> $")
print(amount)
amount = float(amount)

amount = amount*100.00
# have to round the number up, otherwise 115 became 114.99999
amount = round(amount)
amount = int(amount)
print(amount)
quarters = amount//25
amount = amount - quarters*25
print(amount)
dimes = amount//10
print(dimes)
amount = amount - dimes*10
print(amount)
nickles = amount//5
print(nickles)
amount = amount - nickles*5
pennies = amount

qS = "s"
dS = "s"
nS = "s"
pS = "penny"
if quarters == 1:
    qS = ""
if dimes == 1:
    dS = ""
if nickles == 1:
    nS = ""
if pennies != 1:
    pS = "pennies"


print("you have " + str(quarters) + " quarter" + qS + ", " + str(dimes) + " dime" + dS + ", " + str(nickles) + " nickle"
      + nS + " and " + str(pennies) + " " + pS + ".")
