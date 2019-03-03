#practice_string_problems.py

#problem 1
#single = list(input("what do you want us to double for you? >>"))

#double = []
#for i in single:
#    double.append(i * 2)

#print(''.join(double))

#another way

#twoTimes = ''
#
#for i in single:
#    twoTimes += i * 2
#
#
#print(twoTimes)

# problem 2


#full = ["kitten"]
#listed = list(full)
#missing = []
#for i in range(len(full)):
#    word = listed
#
#
#
##problem 3
#
#latest_letter = list('pneumonoultramicroscopicsilicovolcanoconiosis')
#latest_letter.sort()
#print("the latest letter is " + latest_letter[-1])


#problem 6

def count_letter(letter, word):
    count = {letter: 0}
    for i in list(word):
        if i in count:
            count[letter] += 1
    return count[letter]


print(count_letter('a', 'adfadsflkjlajbbalskdfjabalsdkjfoib'))






























