# lab20-Credit_Card_Validation.py

card_number = list("4556737586899855")

for num in range(len(card_number)):
    card_number[num] = int(card_number[num])

check_digit = card_number[-1]
del card_number[-1]
card_number.reverse()
print(card_number)
for i in range(0, len(card_number), 2):
        card_number[i] = card_number[i] * 2
for i in range(len(card_number)):
    if card_number[i] > 9:
        card_number[i] = card_number[i] - 9
total = list(str(sum(card_number)))
if int(total[-1]) == check_digit:
    print("this card is valid.")
elif int(total[-1]) != check_digit:
    print("this is not a valid card number.")

    
print(total)
print(card_number)
#Scheck_number = int(card_number[-1])
#Sdel card_number[-1]
#Scard_number.reverse()
#S
#Sfor i in range(len(card_number)):
#S    if i % 2 == 0:

