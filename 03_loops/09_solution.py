# Problem: Check if all the elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate

# number_of_items = int(input("Enter the number of elements: "))
user_items = ["apple", "banana", "orange", "apple", "mango", "banana"]
unique_item = set()

# for i in range(number_of_items):
#     items = (input(f"Enter element {i+1}: "))
#     user_items.append(items)

for items in user_items:
    if items in unique_item:
        print(items)
        continue
    else:
        unique_item.add(items)


