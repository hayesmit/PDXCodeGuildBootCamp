#lab05-Random_Emotico_Generator
import random

eyes = [" . . \n", " o O\n", " - -\n", " @ @\n"]
nose = ["  U\n", "   - \n", "  ^\n"]
mouth = [' ___\n\n', "  O\n\n", "(___)\n\n"]

x = 0
while x < 5:
    print(random.choice(eyes)+random.choice(nose)+random.choice(mouth))
    x += 1
