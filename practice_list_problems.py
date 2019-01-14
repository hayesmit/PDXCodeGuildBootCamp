#practice_list_problems.py
import random
#players = ['Drexler', 'Jordan', 'Oden', 'James', 'Iverson']
#
#
#def pick_one(option):
#    return random.choice(option)
#
#
#print(pick_one(players))


nums1 = [5, 6, 2]
nums2 = [5, 5, 2]


def even_evens(nums):
    count = 0
    for i in nums:
        if i % 2 == 0:
            count += 1
    if count % 2 == 0:
        print(True)
    elif count % 2 == 1:
        print(False)


even_evens(nums1)
