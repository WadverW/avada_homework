"""
class Conditioner
temp
mode
fan_speed
power
def is_on()
    def start_condition(self):
    return f"Conditioner is on. Temp: {self.temp}, Mode: {self.mode}, Fan Speed: {self.fan_speed}"

class ConditionerBuilder:
    set_temp(self, temp: int)
    set_mode(self, mode: str)
    set_fan_speed(self, fan_speed: str)
    set_power()

"""

from datetime import datetime
import copy


def start_condition(func):
    def wrapper(self, *args, **kwargs):
        if self.is_on():
            start = func(self, *args, **kwargs)
        else:
            return f"<<< Display >>>\n \
            {datetime.now().strftime('%H:%M:%S')}"
        return start

    return wrapper


class Conditioner:
    def __init__(self, temp: int, mode: str, fan: str, power: bool = False):
        self.temp = temp
        self.mode = mode
        self.fan = fan
        self.power = power

    def is_on(self):
        return self.power

    @start_condition
    def start_conditioner(self):
        return f"<<< Display >>>\n \
        Temp: {self.temp}\n \
        Mode: {self.mode}\n \
        Fan: {self.fan}"

    # To apply Prototype pattern
    @start_condition
    def clone(self, shallow: bool = True):
        if shallow:
            return copy.copy(self)
        else:
            return copy.deepcopy(self)


# To apply Builder pattern
class ConditionerBuilder:
    def __init__(self):
        self._temp = 23
        self._mode = "dry"
        self._fan = "medium"
        self._power = False

    def set_temp(self, temp: int):
        self._temp = temp
        return self

    def set_mode(self, mode: str):
        self._mode = mode
        return self

    def set_fan(self, fan: str):
        self._fan = fan
        return self

    def set_power(self):
        self._power = True
        return self

    def build(self):
        if not self._temp or not self._mode:
            raise ValueError("Please setup parameters")
        return Conditioner(
            power=self._power,
            temp=self._temp,
            mode=self._mode,
            fan=self._fan,
        )


if __name__ == "__main__":
    kitchen = (
        ConditionerBuilder()
        .set_power()
        .set_temp(19)
        .set_mode("cool")
        # .set_fan("high")
        .build()
    )

    print(kitchen.start_conditioner())

    bedroom = kitchen.clone(False)
    bedroom.power = True
    bedroom.temp = 23
    bedroom.mode = "cool"
    print(bedroom.start_conditioner())


# Цель: Пошаговая сборка сложного объекта.

# Принцип: Разделение конструирования и представления.

# Плюс: Гибкость в создании разных конфигураций.
