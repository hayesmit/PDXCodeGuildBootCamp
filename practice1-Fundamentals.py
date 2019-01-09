# practice 1 Fundementals.py


#problem 1
def is_even(a):
    return a % 2 == 0


print(is_even(5))
print(is_even(6))


#problem 2
def opposite(a,b):
    return (a > 0 and b < 0) or (a < 0 and b > 0)


print(opposite(10, -1))
print(opposite(2, 3))
print(opposite(-1, -1))


#problem 3
def near_100(num):
    return 90 <= num <= 110

print(near_100(50))
print(near_100(99))
print(near_100(105))


#problem 4
def maximum_of_three(a, b, c):
    vals = [a, b, c]
    return max(vals)


print(maximum_of_three(5, 6, 2))
print(maximum_of_three(-4, 3, 10))


#problem 5
list = []
for i in range(21):
   list.append(2**i)

print(list)
