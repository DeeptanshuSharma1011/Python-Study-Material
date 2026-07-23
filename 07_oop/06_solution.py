# Problem: Add a class variable to Car that keeps track of the number of cars created.

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
    
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

    def specs(self):
        return f"{self.full_name()} - {self.battery_size}"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.specs()) # Tesla Model S - 85kWh
print(my_tesla.fuel_type()) # Electric Charge

new_car1 = Car("Tata", "Safari")
print(new_car1.fuel_type()) # Petrol or Diesel

# storing the reference of the object in a variable (1st way)
new_car2 = Car("Ferrari", "SF90")
print(new_car2.full_name()) # Ferrari SF90

#creating object (2nd way)
Car("Volvo", "XC90")
Car("BMW", "M4 Competition")

print(Car.total_cars) # 5