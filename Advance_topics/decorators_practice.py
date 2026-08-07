
def logger(func):
    def wrap(*args):
        print("Before the greet function.",)
        result = func(*args)
        print("After the greet function.", result)
        return result
    return wrap

@logger
def greet():
    print("Hello, Python!")

greet() 