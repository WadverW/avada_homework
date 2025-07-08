from datetime import datetime
from abc import ABC, abstractmethod


class Conditioner(ABC):
    @abstractmethod
    def start(self) -> bool:
        pass

    @abstractmethod
    def stop(self) -> bool:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @property
    @abstractmethod
    def temp(self) -> int:
        pass

    @temp.setter
    @abstractmethod
    def temp(self, temp: int):
        pass

    @property
    @abstractmethod
    def fan(self) -> str:
        pass

    @fan.setter
    @abstractmethod
    def fan(self, fan: str):
        pass

    @property
    @abstractmethod
    def mode(self) -> str:
        pass

    @mode.setter
    @abstractmethod
    def mode(self, mode: str):
        pass


class Mitsubishi(Conditioner):
    def __init__(
        self, state: bool = False, temp: int = 20, fan: str = "low", mode: str = "dry"
    ):
        self._state = state
        self._temp = temp
        self._fan = fan
        self._mode = mode

    def start(self) -> bool:
        self._state = True
        return self._state

    def stop(self) -> bool:
        self._state = False
        return self._state

    def get_name(self):
        return f"Brand: {self.__class__.__name__}"

    def get_status(self):
        if self._state:
            return f"Temperature: {self.temp}, Fan: {self.fan}, Mode: {self.mode}"
        return datetime.now().strftime("%H:%M") + " (Off)"

    @property
    def temp(self) -> int:
        return self._temp

    @temp.setter
    def temp(self, temp: int):
        if not 0 <= temp <= 30:
            raise ValueError("Temperature must be in the range 0 - 30.")
        self._temp = temp

    @property
    def fan(self) -> str:
        return self._fan

    @fan.setter
    def fan(self, fan: str):
        valid_ = ["low", "medium", "high", "auto"]
        if fan not in valid_:
            raise ValueError("Invalid fan speed")
        self._fan = fan

    @property
    def mode(self) -> str:
        return self._mode

    @mode.setter
    def mode(self, mode: str):
        valid_ = ["cool", "heat", "dry", "fan"]
        if mode not in valid_:
            raise ValueError("Invalid mode")
        self._mode = mode


class Remote:
    def __init__(self, conditioner: Conditioner):
        self._conditioner = conditioner

    def off(self):
        self._conditioner.stop()
        return self

    def on(self):
        self._conditioner.start()
        return self

    @property
    def temp(self):
        return self._conditioner.temp

    @temp.setter
    def temp(self, temp: int):
        if 0 < temp <= 30:
            self._conditioner.temp = temp
        else:
            raise ValueError("Temperature must be 0 - 30")

    def set_fan(self, fan: str):
        self._conditioner.fan = fan
        return self

    def set_mode(self, mode: str):
        self._conditioner.mode = mode
        return self

    def status(self):
        print(self._conditioner.get_status())


if __name__ == "__main__":
    cond = Mitsubishi()
    remote = Remote(cond)

    remote.on()
    remote.temp = 21
    remote.set_fan("medium")
    remote.set_mode("cool")

    print(f"Conditioner {cond.get_name()} - ON")
    remote.status()
    print("=" * 10)

    print(f"Conditioner {cond.get_name()} - OFF")
    remote.off()
    remote.status()
