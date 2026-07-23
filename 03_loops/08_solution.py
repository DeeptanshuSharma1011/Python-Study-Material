# Problem: Check if a number is Prime.

number = int(input("Enter the number: "))

is_Prime = True

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            is_Prime = False
            break

print(is_Prime)