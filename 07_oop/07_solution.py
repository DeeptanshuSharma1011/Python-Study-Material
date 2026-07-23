# Problem: Add a static method to the Car class that returns a general description of the car.

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1
        
    def full_name(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    # these are the decorators (used when to apply any rule, enhance the functionality)
    # dont use the self because it does not work on the class instead work on the object.
    def general_description():
        return "Cars are means of transport"
    
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

print(Car.general_description())
print(my_car.general_description())