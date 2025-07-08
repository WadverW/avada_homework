from enum import Enum
from abc import ABC, abstractmethod
from threading import Thread
import time


class CoffeeType(Enum):
    espresso = 1
    americano = 2
    latte = 3
    cappuccino = 4


# Factory interface
class Coffee(ABC):
    @abstractmethod
    def get_coffee(self):
        pass


class Espresso(Coffee):
    def get_coffee(self):
        time.sleep(1)
        print("Get espresso")


class Americano(Coffee):
    def get_coffee(self):
        time.sleep(1)
        print("Get americano")


class Cappuccino(Coffee):
    def get_coffee(self):
        time.sleep(1)
        print("Get cappuccino")


class Latte(Coffee):
    def get_coffee(self):
        time.sleep(1)
        print("Get latte")


# Coffemachine interface
class CoffeeMachine(ABC):
    @abstractmethod
    def brew_coffee(self, coffee_type: CoffeeType) -> Coffee:
        pass


# Factory class to start making coffee
# based on coffee type
class IncantoBrand(CoffeeMachine):
    def brew_coffee(self, coffee_type: CoffeeType) -> Coffee:
        if coffee_type == CoffeeType.espresso:
            return Espresso()
        elif coffee_type == CoffeeType.americano:
            return Americano()
        elif coffee_type == CoffeeType.latte:
            return Latte()
        elif coffee_type == CoffeeType.cappuccino:
            return Cappuccino()
        else:
            raise ValueError("Unknown coffee type")


# Get each order-item in a separate thread
def order_coffee(coffee: Coffee):
    print(f"Start brewing: {coffee.__class__.__name__}")
    time.sleep(1)
    thread = Thread(target=coffee.get_coffee)
    thread.start()
    return thread


# Input order
def input_order() -> str:
    while True:
        coffee_order = (
            input("Enter coffee type (espresso/americano/latte/cappuccino/exit): ")
            .strip()
            .lower()
        )
        if coffee_order not in ["espresso", "americano", "latte", "cappuccino", "exit"]:
            print("Please enter 'espresso/americano/latte/cappuccino' or 'exit'")
        else:
            return coffee_order


# Main execution
if __name__ == "__main__":
    factory = IncantoBrand()
    entire_order = []  # To store order-items

    while True:
        coffee = None
        coffee_order = None

        try:
            coffee_order = input_order()

            if coffee_order == "espresso":
                coffee = factory.brew_coffee(CoffeeType.espresso)
            elif coffee_order == "americano":
                coffee = factory.brew_coffee(CoffeeType.americano)
            elif coffee_order == "latte":
                coffee = factory.brew_coffee(CoffeeType.latte)
            elif coffee_order == "cappuccino":
                coffee = factory.brew_coffee(CoffeeType.cappuccino)
            elif coffee_order == "exit":
                break
            else:
                continue

            entire_order.append(coffee)
        except ValueError as e:
            print("Error:", e)
            break
        finally:
            if coffee_order != "exit" and coffee is not None:
                print(coffee.__class__.__name__, "preparing...")

    # Get all ordered coffee
    chosen_coffee = [order_coffee(coffee) for coffee in entire_order]
    for t in chosen_coffee:
        t.join()


# отделить код, который создает объекты, от кода, который их использует
# потоки работают конкурентно
