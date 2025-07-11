from abc import ABC, abstractmethod


class Conditioner(ABC):
    @abstractmethod
    def start(self) -> bool:
        pass

    @abstractmethod
    def stop(self) -> bool:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def temp(self) -> int:
        pass

    @temp.setter
    @abstractmethod
    def temp(self, value: int):
        pass

    @property
    @abstractmethod
    def mode(self) -> str:
        pass

    @mode.setter
    @abstractmethod
    def mode(self, value: str):
        pass

    @property
    @abstractmethod
    def fan(self) -> str:
        pass

    @fan.setter
    @abstractmethod
    def fan(self, value: str):
        pass


class Aircool(Conditioner):
    def __init__(self):
        self._name = self.__class__.__name__
        self._is_on = False

        self._temp = 16
        self._mode = "dry"

        self._fan = "medium"

    @property
    def name(self) -> str:
        return self._name

    def start(self) -> bool:
        self._is_on = True
        return self._is_on

    def stop(self) -> bool:
        self._is_on = False
        return self._is_on

    @property
    def temp(self) -> int:
        return self._temp

    @temp.setter
    def temp(self, value: int):
        if not (16 <= value <= 30):
            raise ValueError(f"Temperature must be in [16 - 30] degrees. Got {value}")
        self._temp = value

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, value: str):
        valid = ["dry", "cool", "heat", "fan"]
        if value not in valid:
            raise ValueError("Invalid mode")
        self._mode = value

    @property
    def fan(self) -> str:
        return self._fan

    @fan.setter
    def fan(self, value: str):
        valid = ["low", "medium", "high", "auto"]
        if value not in valid:
            raise ValueError("Invalid fan speed")
        self._fan = value


# === Decorators ===


class DecoratorConditioner(Conditioner):
    def __init__(self, conditioner: Conditioner):
        if not isinstance(conditioner, Conditioner):
            raise TypeError("Invalid object type")
        self._conditioner = conditioner

    @property
    def name(self) -> str:
        return self._conditioner.name

    @property
    def temp(self) -> int:
        return self._conditioner.temp

    @temp.setter
    def temp(self, value: int):
        self._conditioner.temp = value

    @property
    def mode(self) -> str:
        return self._conditioner.mode

    @mode.setter
    def mode(self, value: str):
        self._conditioner.mode = value

    @property
    def fan(self) -> str:
        return self._conditioner.fan

    @fan.setter
    def fan(self, value: str):
        self._conditioner.fan = value

    def start(self) -> bool:
        return self._conditioner.start()

    def stop(self) -> bool:
        return self._conditioner.stop()


class ModeDecorator(DecoratorConditioner):
    def __init__(self, conditioner: Conditioner):
        super().__init__(conditioner)
        print(f"ModeDecorator for {self.name}.")

    @property
    def temp(self) -> int:
        print(f"{self.name} Mode: {self.mode}")
        return super().temp

    @temp.setter
    def temp(self, value: int):
        print(f"{self.name} ModeDecorator sets temperature to {value}.")
        self._conditioner.temp = value


class FanDecorator(DecoratorConditioner):
    def __init__(self, conditioner: Conditioner):
        super().__init__(conditioner)
        print(f"FanDecorator for {self.name}")

    @property
    def temp(self) -> int:
        print(f"{self.name} Fan speed: {self.fan}")
        return super().temp

    @temp.setter
    def temp(self, value: int):
        print(f"{self.name} FanDecorator sets temperature to {value}")
        self._conditioner.temp = value

    def display_settings(self):
        print(f"{self.name} / {self.fan} / {self.mode}")


# === Main Execution ===

if __name__ == "__main__":
    aircool = Aircool()
    aircool.temp = 22
    aircool.fan = "low"
    aircool.mode = "cool"

    mode_decorated = ModeDecorator(aircool)

    fan_decorated = FanDecorator(mode_decorated)

    fan_decorated.start()  # start() passes through all decorators

    print(f"Get temperature: {fan_decorated.temp}")
    print(f"{fan_decorated.name}")
