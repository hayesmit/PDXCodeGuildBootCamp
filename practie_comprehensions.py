#practice_comprehensions.py

#problem 1
#powers_of_two = [2**x for x in range(10)]
#print(powers_of_two)


#problem 3
dictionary = {'a': 1, 'b': 2, 'c': 3}
dictionary = {v: k for k, v in dictionary.items()}
print(dictionary)
