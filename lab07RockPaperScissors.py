#lab07RockPaperScissors.py
import random

win = ["rockscissors", "paperrock", "scissorspaper"]
lose = ["rockpaper", "paperscissors", "scissorsrock"]

def play(me, you):
    if me+you in win:
        print("you win")
    elif me+you in lose:
        print("you lose")
    else:
        print("tie")
x = "yes"
while x == "yes":
    user = input("Choose one: rock, paper or scissors. >>  ")
    computer = random.choice(["rock", "paper", "scissors"])
    play(user, computer)
    x = input("want to play again, if so type yes? >> ")


