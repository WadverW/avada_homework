from abc import ABC, abstractmethod


class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class Music:
    def play(self):
        print("Music is PLAYING")

    def stop(self):
        print("Music is STOPPED")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Concrete command
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class MusicPlayCommand(Command):
    def __init__(self, music: Music):
        self.music = music

    def execute(self):
        self.music.play()

    def undo(self):
        self.music.stop()


class RemoteControl:
    def __init__(self):
        self.history = []

    def run_command(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo_last(self):
        if self.history:
            command = self.history.pop()
            command.undo()
        else:
            print("Nothing to undo")


if __name__ == "__main__":
    light = Light()
    music = Music()

    remote = RemoteControl()

    remote.run_command(LightOnCommand(light))
    remote.run_command(MusicPlayCommand(music))

    remote.undo_last()
    remote.undo_last()
