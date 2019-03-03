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


#problem 3
#nums1 = [5, 6, 2]
#nums2 = [5, 5, 2]
#
#
#def even_evens(nums):
#    count = 0
#    for i in nums:
#        if i % 2 == 0:
#            count += 1
#    return count % 2 == 0
#
#
#even_evens(nums1)



#problem 7
#def common_elements(nums1, nums2):
#    nums1 = set(nums1)
#    nums2 = set(nums2)
#    merge = []
#    for num in nums1:
#        if num in nums2:
#            #if num not in merge:
#            merge.append(num)
#    print(merge)
#
#
#group1 = [1, 2, 4, 55, 82, 6, 5, 4, 3]
#group2 = [4, 7, 8, 82]
#
#common_elements(group1, group2)

#practice 8
#thing1 = ["a", "b", "c"]
#thing2 = [1, 2, 3]
#together = []
#for i in range(len(thing1)):
#    together.append(thing1[i])
#    together.append(thing2[i])
#
#print(together)
#much cooler solution
# together = [i for j in zip(thing1, thing2 for i in j]


#problem 13
#numbers = [1, 2, 5, 8, 8, 6, 3, 4, 0]
#
#def minimum(calculate):
#        calculate.sort()
#        print(calculate[0])
##minimum(numbers)
#
#
#def maximum(calculate):
#    calculate.sort()
#    print(calculate[-1])
#
#
#def mean(calculate):
#    together = sum(calculate)
#    print(together/(len(calculate)))
##mean(numbers)
#
#
#def mode(calculate):
#    frequency = {}
#    for num in calculate:
#        if num not in frequency:
#            frequency[num] = 1
#        elif num in frequency:
#            frequency[num] += 1
#    print(max(frequency.items(), key = lambda x: x[1])[0])
#mode(numbers)


#problem 11
#these = [[1, 2, 3], [5, 6, 7], [8, 9, 4]]
#def combine_all(my_lists):
#    together = []
#    for i in range(len(these)):
#        together.extend(these[i])
#    return together
#
#print(combine_all(these))

#another way
#return reduce(Lambda acc,



# problem 12
return [calc_fib(i for i in range(n))]


def fib(n):
    collection = []
    for i in range(n):
        num = 0
        if n == 0:
            num += 0
        if n == 1:
            num += 1
        if n >= 2:
            num += fib(n-1)+fib(n-2)
        collection.append(str(num))
    return collection

print(fib(8))


















