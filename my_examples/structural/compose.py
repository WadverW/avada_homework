class Unit:
    """
    Unit of wich the multy climate system is assembled
    """

    def __init__(self, name: str, price: float, volume: int):
        self.name = name
        self.price = price
        self.volume = volume
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price
        return self

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, volume: int):
        if volume < 500:
            raise ValueError("Volume must be at least 500 Watt")
        self._volume = volume
        return self


class Composite:
    """
    System of units (out and inner units)
    """

    BRANDS = ["Fujico", "EWT", "Aircool", "Chiq"]

    def __init__(self, name: str):
        self.name = name
        self.units = []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str):
        if name not in self.BRANDS:
            raise ValueError("Brand not found")
        self._name = name
        return self

    def add_unit(self, unit: Unit):
        self.units.append(unit)
        unit.set_parent(self)
        return self

    def price(self) -> float:
        total_price = 0
        for unit in self.units:
            total_price += unit._price
        return total_price


if __name__ == "__main__":
    out_unit = Unit("FMA", 800.0, 1000)
    inner_unit1 = Unit("fma-09", 50.0, 500)
    inner_unit2 = Unit("fma-09", 50.0, 500)
    inner_unit3 = Unit("fma-07", 45.0, 500)

    out_unit2 = Unit("FMA", 800.0, 1000)
    inner_unit11 = Unit("fma-12", 50.0, 500)
    inner_unit22 = Unit("fma-12", 50.0, 500)

    multysystem = Composite("Fujico")

    multysystem.add_unit(out_unit).add_unit(inner_unit1).add_unit(inner_unit2).add_unit(
        inner_unit3
    )

    multysystem.add_unit(out_unit2).add_unit(inner_unit11).add_unit(inner_unit22)

    print(multysystem.price())
    print([x.name for x in multysystem.units])
    # print(out_unit.parent.name)

# Цель: Иерархия «часть-целое» — работа с объектами и группами одинаково.

# Плюс: Упрощает работу с деревьями.
