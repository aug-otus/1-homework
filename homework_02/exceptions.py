"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    print("Mana is low")


class NotEnoughFuel(Exception):
    print("Not enough mana")


class CargoOverload(Exception):
    print("It's too hard")
