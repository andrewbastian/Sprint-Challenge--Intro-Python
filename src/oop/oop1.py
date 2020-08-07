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


class Vehicle:
    """Vehicle IS BASE CLASS"""
    pass


class FlightVehicle(Vehicle):
    """docstring for FlightVehicle"""
    pass


class Starship(FlightVehicle):
    """docstring for Starship"""
    pass


class Airplane(FlightVehicle):
    """docstring for Airplane"""
    pass


class GroundVehicle(Vehicle):
    """docstring for GroundVehicle"""
    pass


class Car(GroundVehicle):
    """docstring for Car"""
    pass


class Motorcycle(GroundVehicle):
    """docstring for Motorcycle"""
    pass
