#lab11-Simple_Calculator.py

#import operator
#again = "yes"
#ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, }

#while again != "done":
#    operation = input("which operation would you like to perform? +, -, *, /  >>  ")
#    firstNumber = float(input("What is the first number? >>  "))
#    secondNumber = float(input("What is your second number? >>  "))
#    print(ops[operation](firstNumber, secondNumber))
#    again = input("Would you like to do another problem? yes or done? >> ")

happy = "yes"
while happy != "done":
    equation = input("give me your equation, example 5 + 6 >>  ")
    print(eval(equation))
    happy = input("Want to ask another? yes or done?  >>  ")
