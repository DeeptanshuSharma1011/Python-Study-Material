
print("Resource opened successfully")

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError as zde:
    print("An error occurred: Cannot divide by zero.", zde)
except ValueError as ve:
    print("An error occurred: Invalid input. Please enter numeric values.", ve)
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    print("Resource closed successfully")

print("END OF THE PROGRAM")