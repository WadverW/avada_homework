# Базовый класс для пользователя
class ChatUser:

    def __init__(self, name: str):
        self.name = name
        self.mediator = None

    def set_mediator(self, med: 'Mediator'):
        self.mediator = med

    def send(self, msg: str):
        print(f"{self.name}: Sending message - {msg}")
        if self.mediator:
            self.mediator.send_message(msg, self)
        else:
            print(f"Error: Mediator not set for {self.name}. Cannot send message.")

    def receive(self, msg: str):
        print(f"{self.name}: Receiving message {msg}")


class Mediator:
    def __init__(self):
        self.users = []

    def add_user(self, user: ChatUser):
        self.users.append(user)
        user.set_mediator(self)

    def send_message(self, msg: str, sender: ChatUser):
        print(f"\nMediator: Message '{msg}' from {sender.name}.")
        for u in self.users:
            if u != sender:
                u.receive(msg)

if __name__ == '__main__':
    chat_mediator = Mediator()

    user1 = ChatUser("Alice")
    user2 = ChatUser("Bob")
    user3 = ChatUser("Carol")

    chat_mediator.add_user(user1)
    chat_mediator.add_user(user2)
    chat_mediator.add_user(user3)

    user1.send("Привет всем!")
    user2.send("Как дела, Элис?")
    user3.send("Отличный день!")