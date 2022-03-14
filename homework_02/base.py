from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    weight: int = 1000
    started: bool = False
    fuel: int = 0
    fuel_consumption: int = 10

    def __init__(self, weight, fuel, fuel_consumption, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if self.started is False:
            if self.fuel == 0:
                raise exceptions.LowFuelError(Exception)
            else:
                self.started = True

    def move(self, dist):
        if dist * self.fuel_consumption > self.fuel:
            raise exceptions.NotEnoughFuel(Exception)
        else:
            self.fuel = self.fuel - dist * self.fuel_consumption
