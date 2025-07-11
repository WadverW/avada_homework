from abc import ABC, abstractmethod


class Spell:
    def summon(self):
        print("Summoning Thing from beyond")

    def send(self):
        print("Sending Thing back to the abyss")


class Protect:
    def fight(self):
        print("fight the Thing")

    def obey(self):
        print("The gamer obeys the Thing from beyond")


# Command ===================
class Action(ABC):
    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def back(self):
        pass


class SpellAction(Action):
    def __init__(self, spell: Spell):
        self.spell = spell

    def forward(self):
        self.spell.summon()

    def back(self):
        self.spell.send()

    def __repr__(self):
        return self.__class__.__name__[:-6]


class ProtectAction(Action):
    def __init__(self, protect: Protect):
        self.protect = protect

    def forward(self):
        self.protect.fight()

    def back(self):
        self.protect.obey()

    def __repr__(self):
        return self.__class__.__name__[:-6]


class Move:
    def __init__(self):
        self.actions = []

    def move_forward(self, action: Action):
        action.forward()
        self.actions.append(action)

    def move_back(self):
        last_action = self.actions.pop()
        last_action.back()

    def clear_history(self):
        self.actions.clear()


if __name__ == "__main__":
    spell = Spell()
    protect = Protect()

    move = Move()

    move.move_forward(SpellAction(spell))
    move.move_forward(ProtectAction(protect))
    move.move_forward(SpellAction(spell))
    move.move_back()

    print("Gamer actions: ", move.actions)


