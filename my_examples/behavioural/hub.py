from abc import ABC, abstractmethod
from gc import enable


class Mediator(ABC):

    @abstractmethod
    def block(self, *args) -> bool:
        pass

    def include(self, *args, **kwargs):
        pass

    def emergency(self):
        pass

class Door(ABC):
    @abstractmethod
    def set_mediator(self, med: Mediator) -> Mediator:
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def shout(self):
        pass

# ===========================
class Exit(Door):
    def __init__(self, id: int, status: bool = True):
        self.id = id
        self.status = status
        self.mediator = None

    def set_mediator(self, mediator: Mediator):
        self.mediator = mediator

    def open(self):
        if not self.mediator:
            if self.status:
                self.mediator.unblock(self.id)

    def shout(self):
        if self.mediator:
            if self.status:
                self.mediator.block(self.id)

class Alarm:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator
        self._on = True

    @property
    def on(self):
        return self._on

    @on.setter
    def on(self, value: bool):
        self._on = value


class Hub(Mediator):
    def __init__(self):
        self._doors = []
        self.alarm = Alarm(self)

    def include(self, door: Exit):
        self._doors.append(door)
        door.set_mediator(self)
        return self

    def emergency(self):
        if self.alarm.on:
            for door in self._doors:
                door.shout()

    def block(self, id: int):
        door_ = self._doors[id - 1]
        door_.status = False
        print(f"Door {id} is blocked!")

    def unblock(self, id: int):
        door_ = self._doors[id - 1]
        door_.status = True
        print(f"Door {id} is unblocked!")


if __name__ == '__main__':
    hub = Hub()

    door_1 = Exit(1)
    door_2 = Exit(2)
    door_3 = Exit(3)

    hub.include(door_1).include(door_2).include(door_3)

    # emergency
    hub.alarm.on = True
    hub.emergency()
    print(door_1.status)
