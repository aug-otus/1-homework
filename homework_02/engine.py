"""
create dataclass `Engine`
"""
import dataclasses


@dataclasses.dataclass
class Engine:
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons
