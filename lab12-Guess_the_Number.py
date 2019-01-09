#lab12-Guess_the_Number.py

import random
#user guesses code lines 5-25
#computer = random.randint(1, 10)
#
#last_guess = 1000
#x = 1
#while x:
#    my_guess = int(input("guess number " + str(x) + " >>  "))
#    if last_guess < 100 and abs(my_guess-computer) > abs(last_guess-computer):
#        print("you are further from the answer than your previous guess.")
#    elif last_guess < 100 and abs(my_guess-computer) < abs(last_guess-computer):
#        print("You are getting closer")
#    if computer == my_guess:
#        print("You got it and it only took you " + str(x) + " guesses.")
#        break
#    elif my_guess > computer:
#        print("too high!")
#        x += 1
#        last_guess = my_guess
#    else:
#        print("to low!")
#        x += 1
#        last_guess = my_guess


my_choice = int(input("pick a number 1-10 and lets see how long it takes a computer to guess it. >>  "))

x = 1
while x:
    computerGuess = random.randint(1, 10)
    if my_choice == computerGuess:
        print("Got it and it only took " + str(x) + " guesses.")
        break
    else:
        x += 1
