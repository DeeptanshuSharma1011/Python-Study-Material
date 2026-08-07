

num = int(input("Enter a number: "))

value = lambda num: num%2 == 0

result = value(num)

if result:
    print("Even")
else:
    print("Odd")