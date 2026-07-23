# Problem: Write a function that greet the user. if no name is provided it should greet with a deafult name

def greet(user = "Sam"):
    return "Greetings!" + " " + user

print(greet()) 
print(greet("Deepu"))