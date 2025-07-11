class Singleton_(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class Keep(metaclass=Singleton_):
    def __init__(self):
        self.messages = []

    def add_message(self, message: str):
        self.messages.append(message)
        print(message)

    def get_messages(self):
        return self.messages


if __name__ == "__main__":
    keep1 = Keep()
    keep1.add_message("First message")

    keep2 = Keep()
    keep2.add_message("Second message")

    print(keep1.get_messages())
