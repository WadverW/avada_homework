from collections.abc import Iterable, Iterator
from typing import List

class SystemUnit:
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return f"Unit #{self.number}"


class SystemIterator(Iterator):
    def __init__(self, system: List[SystemUnit], reverse: bool = False):
        self._reverse = reverse
        self._system = system
        self._index: int = -1 if reverse else 0

    def __next__(self):
        try:
            system_unit = self._system[self._index]
            self._index += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return system_unit


class SystemAggregate(Iterable):
    def __init__(self, amount_units: int = 5):
        self._units = [SystemUnit(i + 1) for i in range(amount_units)]
        print(
            f"The System consists of "
            f"{amount_units} units"
        )

    def amount_units(self) -> int:
        return len(self._units)

    def __iter__(self) -> SystemIterator:
        return SystemIterator(self._units)

    def get_reverse_iter(self) -> SystemIterator:
        return SystemIterator(self._units, True)


if __name__ == "__main__":
    system = SystemAggregate(7)

    for unit in system.get_reverse_iter():
        print(unit)
