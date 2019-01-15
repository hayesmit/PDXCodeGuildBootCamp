# lab19-Black_Jack.py

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
         "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
total = []


while sum(total) < 18:
    if sum(total) == 0:
        total.append(cards[input("What is your first card?  >>  ")])
        total.append(cards[input("What is you second card?  >>  ")])
    elif sum(total) < 17:
        print(str(sum(total)) + " Hit")
        total.append(cards[input("whats your next card? >> ")])
    if 17 < sum(total) < 21:
        print(str(sum(total)) + " is pretty good, you should stay. ")
    elif sum(total) == 21:
        print("winner winner, chicken dinner.")
    elif sum(total) > 21 and 11 in total:
        total.remove(11)
        total.append(1)
    elif sum(total) > 21:
        print(str(sum(total)) + " you went over 21, you lose")
