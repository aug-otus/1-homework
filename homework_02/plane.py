"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo = 0
    max_cargo = 2000

    def __init__(self, weight=Vehicle.weight, fuel=Vehicle.fuel, fuel_consumption=Vehicle.fuel_consumption, max_cargo=max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo_new):
        if cargo_new + self.cargo <= self.max_cargo:
            self.cargo += cargo_new
        else:
            raise exceptions.CargoOverload(Exception)

    def remove_all_cargo(self):
        last_cargo = self.cargo
        self.cargo = 0
        return last_cargo
