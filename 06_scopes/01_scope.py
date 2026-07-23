username = "deepu"

def func():
    username = "sharma"
    print(username)

print(username)
func()


x = 99
def func2(y):
    z = x + y
    return z

result = func2(1)
print(result)


def func3():
    global x #never use global values like this (bad practice)
    x = 10

func3()
print(x)


def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()


def f1():
    x = 88
    def f2():
        print(x)
    return f2()
myResult = f1()
myResult()
# this calls the function but it gives 88 because of closure
# clisure means even the f2 function is call it still have the reference numbers/ids of the whole function it is in. 

def coder(num):
    def actual(x):
        return x ** num
    return actual

f = coder(2)
g = coder(3)