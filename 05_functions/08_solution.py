# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key:value

def print_kwargs(**kwargs):
    for key, value in kwargs.items(): 
        # syntax used in **kwargs
        print(f"{key}: {value}")

print_kwargs(name = "thor", power="hammer")
print_kwargs(name = "thor")
print_kwargs(name = "thor", power = "hammer", enemy = "Thanos")

# kwargs used to give output for multiple arguments in key value pair