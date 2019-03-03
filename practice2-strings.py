# practice2-strings.py


#problem1
#def double_letters(x):
#    list(x)
#    final = []
#    for i in x:
#        final.append(i)
#        final.append(i)
#    return ''.join(final)
#
#
##print(double_letters('hello'))
#
#
##problem 2
#def missing_char(x):
#    word = list(x)
#    for i in word:
#        missing = [''.join(word(i).pop())]
#    return missing
#
#
#print(missing_char("hello"))



#problem3
def latest_letter(word):
    word = list(word)
    word.sort()
    print(word[-1])

latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis")
