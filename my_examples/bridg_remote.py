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


class Mitsubishi(Conditioner):
    def __init__(
        self, state: bool = False, temp: int = 20, fan: str = "low", mode: str = "dry"
    ):
        self._state = state
        self.temp = temp
        self.fan = fan
        self.mode = mode

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
            return f"Temperature: {self._temp}, Fan: {self._fan}, Mode: {self._mode}"
        return datetime.now().strftime("%H:%M")


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
        return self._conditioner._temp

    @temp.setter
    def temp(self, temp: int):
        if 0 < temp <= 30:
            self._conditioner._temp = temp
        else:
            raise ValueError("Temperature must be > 0 and < 30")

    def set_fan(self, fan: str):
        self._conditioner._fan = fan
        return self

    def set_mode(self, mode: str):
        self._conditioner._mode = mode
        return self

    def status(self):
        print(self._conditioner.get_status())


if __name__ == "__main__":
    cond = Mitsubishi()
    remote = Remote(cond)
    remote.on()
    remote.temp = 21
    print(f"Conditioner {cond.get_name()} - ON")
    remote.status()
    print("=" * 10)
    print(f"Conditioner {cond.get_name()} - OFF")
    remote.off()
    remote.status()
