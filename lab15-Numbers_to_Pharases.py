# lab15-Numbers_to_Pharases.py

onesPlace = {0: "zero", 1: 'one', 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
tensPlace = {0: '', 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
teenVals = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
            17: "seventeen", 18: "eighteen", 19: "nineteen"}


def convert(my_num):
    response = []
    while my_num >= 0:
        if 0 <= my_num < 10:
            response.append(str(onesPlace[my_num]))
            my_num = my_num - 11
        if 9 < my_num < 20:
            response.append(str(teenVals[my_num]))
            my_num -= my_num - 1
        if 100 > my_num > 20:
            response.append(str(tensPlace[my_num // 10]) + " ")
            my_num = my_num % 10
        if 1000 > my_num >= 100:
            response.append(str(onesPlace[my_num // 100] + " hundred "))
            my_num = my_num % 100
    print(''.join(response))


convert(int(input("what number would you like me to type out for you?")))


