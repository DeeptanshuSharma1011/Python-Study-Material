# Problem: Keep asking the user for input until they enter a number between 1 to 10.

user_input = int(input("Enter the number: "))

while user_input > 10:
    print("Invalid Input")
    user_input = int(input("Enter the number: "))
