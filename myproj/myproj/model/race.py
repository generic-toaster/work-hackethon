from enum import Enum

class Race(Enum):
    human = 1
    dwarf = 2
    elf = 3
    halfElf = 4

    def describe(self):
        return self.name, self.value