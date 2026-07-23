# Problem: Calculate the sum of Even numbers up to given number n.

number = int(input("Enter the number: "))
sum = 0

for i in range(1, number+1):
    if i%2 == 0:
        sum += 1

print(sum)