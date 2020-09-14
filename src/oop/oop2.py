# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.

class GroundVehicle():
    def __init__(self, num_wheels = 4):
        self.num_wheels = num_wheels
    def drive(self):
        return f"vroooom"
    def __str__(self):
        return f"This vehicle has {self.num_wheels} wheels..."
ground_vehicle = GroundVehicle()

print(ground_vehicle, ground_vehicle.drive())

    # TODO

class Motorcycle(GroundVehicle):
    def __init__(self, name, num_wheels = 2):
        super().__init__(num_wheels)
        self.name = name
    def drive(self):
        return f"BRAAAP!!"
    def __str__(self):
        return f"And this vehicle has {self.num_wheels} wheels..."
motorcycle = Motorcycle('Fast')

print(motorcycle, motorcycle.drive())

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

# TODO

vehicles = [
    str(GroundVehicle()),
    str(GroundVehicle()),
    str(Motorcycle("Monster")),
    str(GroundVehicle()),
    str(Motorcycle("Beast")),
]

print( vehicles)
# Go through the vehicles list and print the result of calling drive() on each.

# TODO
