
def log_deco(func):
    def wrap(*args):
        print("values ", args)
        result = func(*args)
        print("Result: ", result)
        return result
    return wrap

def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return wrap

@log_deco
@greater_first
def sub(a,b):
    return a-b

@log_deco
@greater_first
def divide(a,b):
    return a/b


@log_deco
def add(*args):
    return sum(args)


# sub = greater_first(sub)
# divide = greater_first(divide)

result = divide(8,24)
print("Division: ", result)

result2 = sub(2,4)
print("Subtraction: ",result2)

result3 = add(5,7,9,1,20)
print("Addition: ", result3)