''' Task 1: Defind a class namd Car with attributes: make, model, year.
    Conditions:
    - Initialise these attrivutes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
'''

# Knowledge library:
    # - A class is a blueprint for creating objects. The class describes what the object can have (its attributes) and what it can do (its methods). It's like an architect's drawing — it doesn't represent any specific house, just the design.

    # - An instance is an actual object built from the blueprint.


# Define a new class called Car 
class Car: 
    
    # Define initializer method and corresponding attributes
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    # Defind second method
    def describe_car(self):
        print(f"{self.year} {self.model} {self.make}")

''' Task 2: Create an instance of the Car class with the following attributes and call describe_car method:
    - Make: Toyota, 
    - Model: Corolla,
    - Year: 2020
'''

my_car = Car(make="Toyota", model="Corolla", year=2020)
my_car.describe_car()
 