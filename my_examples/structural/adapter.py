import sqlite3
from abc import ABC, abstractmethod


class CustomDBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def insert_user(self, user_id: int, name: str):
        pass

    @abstractmethod
    def fetch_all_users(self):
        pass


class SQLiteAdapter(CustomDBInterface):
    def __init__(self, db_path="test.sqlite3"):
        self.db_path = db_path
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
        self.conn.commit()

    def insert_user(self, user_id: int, name: str):
        self.cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user_id, name))
        self.conn.commit()

    def fetch_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        result = self.cursor.fetchall()
        return result


class App:
    def __init__(self, db: CustomDBInterface):
        self.db = db

    def run_commands(self):
        self.db.connect()
        self.db.insert_user(1, "Rex")
        self.db.insert_user(2, "DDD")
        users = self.db.fetch_all_users()
        for user in users:
            print(f"User: {user}")


# === Запуск ===
if __name__ == "__main__":
    sqlite_adapter = SQLiteAdapter()
    app = App(sqlite_adapter)
    app.run_commands()
