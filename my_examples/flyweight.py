class WhiskeyType:  # ---> General State
    """Whiskey Type - FlyWeight"""

    def __init__(self, brand: str, strength: float, barrel: str, recipe: str):
        self.brand = brand
        self.strength = strength
        self.barrel = barrel
        self.recipe = recipe

    def display(self, batch_number: str, bottle_number: int, bottled_date: str):
        print(
            f"Brand: {self.brand}, Strength: {self.strength}%, Barrel: {self.barrel}, Recipe: {self.recipe} --> "
            f"Batch: {batch_number}, Bottle: {bottle_number}, Bottled date: {bottled_date}"
        )


class WhiskeyFactory:
    """Factory - get or create type (WhiskeyType obj)"""

    def __init__(self):
        self._types = {}

    def get_whiskey_type(self, brand, strength, barrel, recipe):
        type_ = (brand, strength, barrel, recipe)
        if type_ not in self._types:
            print(f"New Type: {type_}")
            self._types[type_] = WhiskeyType(brand, strength, barrel, recipe)
        else:
            print(f"Use Type: {type_}")
        return self._types[type_]


class WhiskeyBottle:
    """Particular bottle -> object (accepts type and external data)"""

    def __init__(
        self,
        number: str,
        bottle_number: int,
        bottled_date: str,
        whiskey_type: WhiskeyType,
    ):
        self.batch_number = number
        self.bottle_number = bottle_number
        self.bottled_date = bottled_date
        self.whiskey_type = whiskey_type

    def display(self):
        self.whiskey_type.display(
            self.batch_number, self.bottle_number, self.bottled_date
        )


# Роль: Distillery uses WhiskeyFactory -> WhiskeyType
# Distillery — client class
class Distillery:
    """Production"""

    def __init__(self, factory: WhiskeyFactory):
        self.bottles = []
        self.factory = factory

    def produce_bottle(
        self, brand, strength, barrel, recipe, number, bottle_number, bottled_date
    ):
        whiskey_type = self.factory.get_whiskey_type(
            brand, strength, barrel, recipe
        )  # get type
        bottle = WhiskeyBottle(
            number, bottle_number, bottled_date, whiskey_type
        )  # create bottle
        self.bottles.append(bottle)  # collect bottles

    def show_all_bottles(self):
        for bottle in self.bottles:
            bottle.display()


# === Use ===

factory = WhiskeyFactory()
distillery = Distillery(factory)

# Produce 4 (3 and 2) bottles
for i in range(1, 4):
    distillery.produce_bottle(
        brand="Glen Fidich",
        strength=40.0,
        barrel="Cherry",
        recipe="Kraft",
        number="AAA1000" + str(i),
        bottle_number=i,
        bottled_date="2025-07-07",
    )

###
for i in range(1, 3):
    distillery.produce_bottle(
        brand="Jameson",
        strength=43.0,
        barrel="Stout",
        recipe="Kraft",
        number="DDD5555" + str(i),
        bottle_number=1,
        bottled_date="2025-07-07",
    )


print("\nAll bottles:")
distillery.show_all_bottles()


# Цель: Экономия памяти за счёт совместного использования общего состояния.

# Принцип: Делит состояние на внешнее и внутреннее.

# Плюс: Снижение количества объектов.
