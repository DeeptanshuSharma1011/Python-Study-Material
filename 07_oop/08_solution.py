# Problem: Use a property decorator in the Car class to make the model attribute read-only

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_cars += 1
        
    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

    def specs(self):
        return f"{self.full_name()} - {self.battery_size}"

ElectricCar("Tesla", "Model S", "85kWh")
Car("Tata", "Safari")
Car("Ferrari", "SF90")
Car("Volvo", "XC90")
my_car = Car("BMW", "M4 Competition")

# attributes can be accessed and changed
# my_car.model = "340i"
print(my_car.model) # now it can be accessed like a property because of the deocrator
print(my_car.full_name())

# after putting the property decorator the attribute became read only (no over-write) also by making it private