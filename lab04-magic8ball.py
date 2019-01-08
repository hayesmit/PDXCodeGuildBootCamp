#lab04-magic8ball.py
import random

again = "yes"
posibilities = ["It is certain", "Without a doubt", "Most likely", "Yes", "No Way", "In your dreams", "Try again later"]

while again != "done":
    input("What is it that the magic 8 ball can help you with? >> ")
    print(random.choice(posibilities)+"\n")
    again = input("Would you like to play again? type yes or done?")
