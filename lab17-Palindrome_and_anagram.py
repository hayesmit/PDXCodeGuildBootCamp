#lab17-Palindrome_and_anagram.py
import string

alpha = string.ascii_lowercase

def check_palindrome(word):
    word = list(word)
    forward = word
    word.reverse()
    palindrome = word
    if forward == palindrome:
        print("yes this is a palindrome")


def check_anagram(arg1, arg2):
    arg1 = list(arg1)
    arg2 = list(arg2)
    letters1 = [i for i in arg1 if i in alpha]
    letters1.sort()
    letters2 = [i for i in arg2 if i in alpha]
    letters2.sort()
    if letters1 == letters2:
        print("yep this is an anagram. ")
    else:
        print("Nope, not an anagram")

PorA = input("want to check for palindrome or anagram? >>  ")
if PorA == "palindrome":
    check_palindrome(input("what do you want to check to see if it is a palindrome? >> "))
elif PorA == "anagram":
    check_anagram(input("first cluster? >>  "), input("second cluster?  >>  "))
