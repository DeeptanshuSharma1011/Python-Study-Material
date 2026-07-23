# Problem: Create a function that returns both the area and circumference of a circle given its radius

# Circumference = 2 * 3.14 * r
# Area = 3.14 * r * r

import math
from decimal import Decimal


def circle(radius):
    area = 2 * radius ** 2
    circumference = (math.pi * radius ** 2)
    return area, circumference

result = int(input("Enter the value of radius: "))

a, c = circle(result)

print("Area: ", a)
print("Circumference: ", c)


# def circle(radius):
#     return "Circumference: ", (math.pi * radius ** 2), "Area: ", (2 * radius ** 2)

# radius = int(input("Enter the size of radius: "))

# result = (circle(radius))
# print(circle(radius))
