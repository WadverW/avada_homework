from abc import ABC, abstractmethod


#
class Car:
    def __init__(self, brand: str, year: int, brands: list[str]):
        self.brand = brand
        self.year = year
        self.brands = brands

# def get_category(car: Car):
#     if car.year < 2000 and car.brand in brands:
#         return Budget
#     elif car.year < 2000 and car.brand not in brands:
#         return Medium
#     elif car.year > 2000 and car.brand in brands:
#         return Premium
#     else:
#         return Budget
#
class CategoryHandler(ABC):
    def __init__(self, handler=None):
        self.handler = handler

    @abstractmethod
    def handle(self, car: Car):
        pass


# Concrete Handlers ======================
class BudgetHandler(CategoryHandler):
    def handle(self, car: Car):
        if car.year < 2000 and car.brand in car.brands:
            return "Budget"
        elif self.handler:
            return self.handler.handle(car)


class MediumHandler(CategoryHandler):
    def handle(self, car: Car):
        if car.year < 2000 and car.brand not in car.brands:
            return "Medium"
        elif self.handler:
            return self.handler.handle(car)


class PremiumHandler(CategoryHandler):
    def handle(self, car: Car):
        if car.year >= 2000 and car.brand in car.brands:
            return "Premium"
        elif self.handler:
            return self.handler.handle(car)


class DefaultHandler(CategoryHandler):
    def handle(self, car: Car):
        return "Budget"


# Make a chain =======================
def compose_category_chain():
    return BudgetHandler(MediumHandler(PremiumHandler(DefaultHandler())))


if __name__ == "__main__":
    cars = [
        Car("toyota", 1995, ["toyota", "volvo", "nissan"]),
        Car("bmw", 1995, ["toyota", "volvo", "nissan"]),
        Car("toyota", 2022, ["toyota", "volvo", "nissan"]),
        Car("peugeot", 2021, ["toyota", "volvo", "nissan"]),
    ]

    chain = compose_category_chain()

    for car in cars:
        category = chain.handle(car)
        print(f"{car.brand} ({car.year}) → {category}")
