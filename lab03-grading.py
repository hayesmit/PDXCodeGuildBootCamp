#lab03-grading.py

grade = int(input("out of 100 what did the student score? >> "))
mod = grade%10
if mod == 9:
    specificGrade = '+'
elif mod == 1 or 0:
    specificGrade = "-"
else:
    specificGrade =""

if grade >= 100:
    print("A+")
elif grade >= 90:
    print("A" + specificGrade)
elif grade >= 80:
    print("B" + specificGrade)
elif grade >= 70:
    print("C" + specificGrade)
elif grade >= 60:
    print("D" + specificGrade)
else:
    print("F")
