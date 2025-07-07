from abc import ABC, abstractmethod
from datetime import datetime


class Conditioner(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @property
    @abstractmethod
    def temp(self):
        pass


class Aircool(Conditioner):
    def __init__(self, temp, mode: str = "dry", fan: str = "low"):
        self.name = self.__class__.__name__
        self.temp = temp
        self.mode = mode
        self.fan = fan

    def start(self):
        return True

    def stop(self):
        return False

    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        if temp < 16 or temp > 30:
            raise ValueError("Temperature must be in [16 - 30] degrees")
        self._temp = temp
        return self._temp


# Decorators


class DecoratorConditioner(Conditioner):
    def __init__(self, conditioner):
        self._conditioner = conditioner

    @property
    def temp(self):
        return self._conditioner.temp

    @temp.setter
    def temp(self, value):
        print("Setting temperature -> ", value)
        self._conditioner.temp = value

    def start(self):
        print("Conditioner is ON")
        return self._conditioner.start()

    def stop(self):
        print("Conditioner is OFF")
        return self._conditioner.stop()


class ModeDecorator(DecoratorConditioner):
    def temp(self):
        if self._conditioner.start():
            print(f"{self._conditioner.name}: mode -> {self._conditioner.mode}")
            super().temp
        if self._conditioner.stop():
            print(datetime.now().strftime("%H:%M"))


class FanDecorator(DecoratorConditioner):
    def temp(self):
        if self._conditioner.fan:
            print(f"{self._conditioner.name}: fan speed -> {self._conditioner.fan}")
            super().temp


if __name__ == "__main__":
    conditioner = Aircool(20)

    deco = DecoratorConditioner(conditioner)
    mode = ModeDecorator(conditioner)
    fan = FanDecorator(conditioner)

    print(fan.start())

# Цель: Динамически добавляет поведение объекту.

# Принцип: Оборачивает объект в другой с расширением функционала.

# Плюс: Альтернатива наследованию.
