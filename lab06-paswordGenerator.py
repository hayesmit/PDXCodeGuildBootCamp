#lab06-PasswordGenerator.py
import string
import random
from random import shuffle

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
numbers = list(string.digits)
symbols = list(string.punctuation)

pLower = int(input("how many lowercase letters would you like in your password?  >> "))
pUpper = int(input("how many uppercase letters would you like in your password?  >> "))
pNumbers = int(input("how many numbers would you like in your password?  >> "))
pSymboles = int(input("how many symbols would you like in your password?  >> "))
myPassword = []
x = 0
while x < pLower:
    myPassword.append(random.choice(lower))
    x += 1

x = 0
while x < pUpper:
    myPassword.append(random.choice(upper))
    x += 1

x = 0
while x < pNumbers:
    myPassword.append(random.choice(numbers))
    x += 1

x = 0
while x < pSymboles:
    myPassword.append(random.choice(symbols))
    x += 1

random.shuffle(myPassword)
myPassword = ''.join(myPassword)
print(myPassword)

