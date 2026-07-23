# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra Shot" of expresso

coffee_type = ("black", "espresso", "latte", "frappe", "capucinno")
coffee_type = input("Enter the type of coffee: ")

coffee_size = ("small", "medium", "large")
coffee_size = input("Enter the size of the coffee: ")

extra_shot = True

if extra_shot:
    coffee_type = coffee_size + " " + coffee_type + " with an extra shot"
else:
    coffee_type = coffee_size + " coffee"

print("Order: ", coffee_type)