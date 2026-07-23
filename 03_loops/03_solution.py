# Problem: Print the multiplication table for a given number upto 10, but skip the fifth iteration

number = int(input("Enter the number: "))

for i in range(1, 11):
    if i != 5:
        answer = number * i
        print(number, "x", i, "=", answer)
    else:
        answer += 1



# if i == 5:
    # continue