# Problem: Recommend a type of pet food based on the pet's species and age. (eg. Dog: < 2 years- Puppy food, Cat: > 5 years- Senior Cat food)

pet_type = ("dog", "cat", "rabbit")
pet_type = input("Enter the pet type: ")
pet_age = int(input("Enter the age of the pet: "))

if pet_age <= 2:
    pet_food = "Puppy "+ pet_type + " food"
elif pet_age >= 5:
    pet_food = "Adult "+ pet_type + " food"
else:
    pet_food = "Anything"

print("Recommendation: ", pet_food)