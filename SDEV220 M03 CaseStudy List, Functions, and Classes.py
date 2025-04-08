"""
Colten Feller
SDEV 220
April 7, 2025
MO3 Case Study - Lists, Functions, and Classes
"""

# import source code 
import random 

# Define the super class called Vehicle
class Vehicle():
    def __init__(self, vehicleType):
        self.vehicleType = vehicleType

    def displayInfor(self):
        print("Vehicle Type: " + self.vehicleType) # print the vehicle type

class Automobile(Vehicle):
    # Initialize the Automobile object with its attributes
    def __init__(self, vehicleType, year, make, model, doors, roof):
        # Initialize inherited attributes
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    # Displays information of the automobile
    def displayInformation(self):
        super().displayInfor()
        print("Year: " + str(self.year))
        print("Make: " + str(self.make))
        print("Model: " + str(self.model))
        print("Doors: " + str(self.doors))
        print("Roof: " + str(self.roof))

# Define functino of teh vehicle app
def VehicleApp():
    vehicleType = input("Enter the Vehicle Type: ")

    year = input("Enter the year of the vehicle: ")
    make = input("Enter the make of the vehicle: ")
    model = input("Enter the model of the vehicle: ")
    doors = input("Enter the door amount of the vehicle: ")
    roof = input("Enter if the vehicle has a sun roof or solid roof: ")


    customerAutomobile = Automobile(vehicleType, year, make, model, doors, roof)

    customerAutomobile.display_info()

VehicleApp()
