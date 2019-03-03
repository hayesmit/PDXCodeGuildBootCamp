n = 10


def func():
    global n
    n += 4


func()
print(n)
