# Problem: Write a decorator that measures the time a function takes to execute.

import time 

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time") # func.__name__ print the name of the function 
        return result
    return wrapper


@timer
# what it does
# it makes this function pass through the timer function
def example_function(n):
    time.sleep(n)

example_function(2)