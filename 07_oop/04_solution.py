# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# 'get' can be used in its own class but can't be used in an object created outside that class. 
# to make a attribute private use __ in front of it (eg. __brand, __method)
# to access the private attribute outside the class we use the getter method. (eg. get_brand, get_method)

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        
    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return f"{self.__brand} !"
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def specs(self):
        return f"{self.full_name()} - {self.battery_size}"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.specs())
print(my_tesla.get_brand())