# Problem: Create a car class with attributes like brand and model. Then create an instance of this class

class Car:
    def __init__(self, brand, model):   #self used to connect the class and its declared variables
                                        # __init__ is the initializer of the class. also called the constructor. called when a new object is formed in a class
        self.brand = brand
        self.model = model
        

my_car = Car("bmw", "m4 comp")
print(my_car.brand, my_car.model)


my_new_car = Car("Rolls-Royce", "Phantom")
print(my_new_car.brand, my_new_car.model)