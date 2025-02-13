"""
    Create a Vehicle class with attributes make and model.
    Create a class hierarchy Vehicle → Car and Bike.
    Add a subclass Car that includes num_doors and overrides a describe() method.
    Implement methods that highlight polymorphism.
    Ensure encapsulation is used for sensitive attributes.
"""

class Vehicle:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
        
    def describe(self):
        return f"{self.__make} {self.__model}"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.__num_doors = num_doors

    def describe(self):
        return f"{super().describe()} with {self.__num_doors} doors"
    
    
class Bike(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model)

    def describe(self):
        return f"{super().describe()} is a bike"
    


def main():
    vehicles = [
        Car("Toyota", "Camry", 4),
        Bike("Yamaha", "MT-07"),
        Car("Honda", "Accord", 2),
        Bike("Ducati", "Panigale V4")
    ]

    for vehicle in vehicles:
        print(vehicle.describe())

if __name__ == "__main__":
    main()
