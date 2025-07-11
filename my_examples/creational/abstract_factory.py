from abc import ABC, abstractmethod


class Sedan(ABC):
    @abstractmethod
    def chose_sedan(self):
        pass


class OffRoad(ABC):
    @abstractmethod
    def chose_offroad(self):
        pass


# Toyota ==============================

class ToyotaSedan(Sedan):
    def chose_sedan(self):
        print("Toyota Camry")


class ToyotaOffRoad(OffRoad):
    def chose_offroad(self):
        print("Toyota RAV4")

# Lexus ===========================

class LexusSedan(Sedan):
    def chose_sedan(self):
        print("Lexus ES")


class LexusOffRoad(OffRoad):
    def chose_offroad(self):
        print("Lexus RX")


# Abstract Factory ====================

class CarFactory(ABC):
    @abstractmethod
    def chose_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def chose_offroad(self) -> OffRoad:
        pass


# Concrete Factory =========================

class ToyotaFactory(CarFactory):
    def chose_sedan(self) -> Sedan:
        return ToyotaSedan()

    def chose_offroad(self) -> OffRoad:
        return ToyotaOffRoad()

#
class LexusFactory(CarFactory):
    def chose_sedan(self) -> Sedan:
        return LexusSedan()

    def chose_offroad(self) -> OffRoad:
        return LexusOffRoad()



class TestDrive:
    def __init__(self, factory: CarFactory):
        self.sedan = factory.chose_sedan()
        self.offroad = factory.chose_offroad()

    def test_drive(self):
        self.sedan.chose_sedan()
        self.offroad.chose_offroad()



if __name__ == "__main__":
    brand = input("Choose a brand (toyota / lexus): ").strip().lower()

    if brand == "toyota":
        factory = ToyotaFactory()
    elif brand == "lexus":
        factory = LexusFactory()
    else:
        raise ValueError("Unknown brand")

    test_drive = TestDrive(factory)
    test_drive.test_drive()
