# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        # joined the values separated by ","
        # iterated the args in a loop and convereted them into a string
        # as the output is expected to be in list so it is mentioned string

        kwargs_value = ", ".join(f"{k}={v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)

    return wrapper





@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

@debug
def hello():
    print("Hello")

hello()
greet("Deepu", greeting="Namaste")
greet("Deepu")

# if there is a function with no arguments then the wrapper will have no *args and **kwargs mentioned in the arguments

# def wrapper():
#         return func()

# def hello():
#      print("Hello")