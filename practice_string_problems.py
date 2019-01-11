#practice_string_problems.py

#problem 1
single = list(input("what do you want us to double for you? >>"))

#double = []
#for i in single:
#    double.append(i * 2)

#print(''.join(double))

#another way

twoTimes = ''

for i in single:
    twoTimes += i * 2


print(twoTimes)
