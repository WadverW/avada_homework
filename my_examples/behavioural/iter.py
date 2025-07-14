from abc import ABC, abstractmethod
from typing import List


class SystemUnit:
    def __init__(self, number: int):
        self.number = number

    def __repr__(self):
        return f"Unit #{self.number}"


class Iterator(ABC):
    @abstractmethod
    def next(self) -> SystemUnit:
        ...

    @abstractmethod
    def has_next(self) -> bool:
        ...


class UnitsIterator(Iterator):
    def __init__(self, system: List[SystemUnit]):
        self._system = system
        self._index = 0

    def next(self) -> SystemUnit:
        unit = self._system[self._index]
        self._index += 1
        return unit

    def has_next(self) -> bool:
        return False if self._index >= len(self._system) else True


class SystemAggregate:
    def __init__(self, units: int = 10):
        self._units = [SystemUnit(i + 1) for i in range(units)]

    def amount_units(self) -> int:
        return len(self._units)

    def iterator(self) -> Iterator:
        return UnitsIterator(self._units)


if __name__ == "__main__":
    units = SystemAggregate(5)
    iterator = units.iterator()
    while iterator.has_next():
        unit = iterator.next()
        print(unit)

# Итератор — это поведенческий паттерн проектирования,
# который даёт возможность последовательно обходить элементы составных объектов,
# не раскрывая их внутреннего представления.