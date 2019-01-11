#practice_list_problems.py
import random
players = ['Drexler', 'Jordan', 'Oden', 'James', 'Iverson']


def pick_one(option):
    return random.choice(option)


print(pick_one(players))
