
def square(num):
    return num * num

def operate(nums, operation):
    return [operation(num) for num in nums]

nums = int(input("Enter the number of elements in the list: "))

numbers = []

for i in range(nums):
    numbers.append(int(input("Enter the number: ")))

result = operate(numbers, square)

print("Original List:", numbers)
print("Squared List:", result)
