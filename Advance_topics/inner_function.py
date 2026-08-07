
def outer():
    print("This is the outer function")

    def inner(num):
        print("This is the inner function", num)

    return inner


something = outer()
something(5)