# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#a this is the root
class Vehicle:
    pass

#a --- the root is Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        pass

#a -- the root is FlightVehicle
class Airplane(FlightVehicle):
    pass

#a -- the root is Vehicle
class GroundVehicle(Vehicle):
    pass

#a --- the root is GroundVehicle
class Car(GroundVehicle):
    pass

#a -- the root is GroundVehicle
class Motorcycle(GroundVehicle):
    pass

#a -- the root is FlightVehicle
class Starship(FlightVehicle):
    pass