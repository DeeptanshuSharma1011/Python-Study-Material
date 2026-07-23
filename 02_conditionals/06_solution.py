# Problem: Choose a mode of transportation based on the distance (eg. <3 km: Walk, 3-15 km: Bike, >15 km: Car)

transportation = ("Walk", "Bike", "Car")
distance_in_kms = int(input("Enter the distance: "))

if distance_in_kms < 3:
    transportation = "Walk"
elif distance_in_kms < 16:
    transportation = "Bike"
else:
    transportation = "Car"

print(transportation)