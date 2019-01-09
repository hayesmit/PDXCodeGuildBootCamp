#lab10_Average_Numbers.py


nums = []
total = 0

newVal = 0
while newVal != "done":
    newVal = input("plug in a number or if you have entered all the numbers you wanted type done. >> ")
    if newVal != "done":
        nums.append(int(newVal))


for i in nums:
    total += i

divide_by = len(nums)

print(total/divide_by)
