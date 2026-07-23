# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance

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

my_car = ElectricCar("Tesla", "S Plaid", "85kWh")


class Battery:
    def battery_info(self):
        return "This is Battery"

class Engine:
    def engine_info(self):
        return "This is Engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_car = ElectricCarTwo("Lamborghini", "Revuelto")
print(my_new_car.battery_info())
print(my_new_car.engine_info())