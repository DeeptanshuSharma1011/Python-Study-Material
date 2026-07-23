# Problem: Suggest an activity based on the weather (eg. Sunny - go for a walk, Rainy - read a book, Snowy - Build a snowman)
import random

weather = ["Sunny", "Rainy", "Snowy"]
weather = input('Enter the weather: ')

Sunny = ["Go for a walk", "Play Cricket", "Meet friends"]
Rainy = ["Read a book", "Eat pakoras with tea", "Rain gaze"]
Snowy = ["Build a snowman", "Drink Hot Chocolate", "Sit by fireplace"]


if weather == "Sunny":
    print(random.choice(Sunny))
elif weather == "Rainy":
    print(random.choice(Rainy))
elif weather == "Snowy":
    print(random.choice(Snowy))