# practice_dictionary_problems.py

#problem 1
player = ['jordan', 'labrron', 'kobey', 'oden', 'drexler']
their_number = [23, 8, 12, 45, 6]


def make_dictionary(key, value):
    return dict(zip(key, value))


my_dictionary = make_dictionary(player, their_number)
print(my_dictionary)
