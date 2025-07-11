from abc import ABC, abstractmethod
import sqlite3


class DBInterface(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass


class Database_(DBInterface):
    def __init__(self, db_name="my_db.sqlite3"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
        self.cursor.executemany(
            "INSERT INTO users (id, name) VALUES (?, ?)",
            [(1, "Cat100"), (2, "Rex1899"), (3, "Wadver")],
        )
        self.conn.commit()

    def get_user_by_id(self, user_id: int):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return self.cursor.fetchone()


class DBProxy(DBInterface):
    def __init__(self, my_db: Database_):
        self.my_db = my_db
        self._cache = {}

    def get_user_by_id(self, user_id: int):
        if user_id in self._cache:
            print(f"Get result from cache for user: {user_id}")
            return self._cache[user_id]

        result = self.my_db.get_user_by_id(user_id)
        self._cache[user_id] = result
        return result


if __name__ == "__main__":
    new_db = Database_()
    proxy_db = DBProxy(new_db)

    print(proxy_db.get_user_by_id(1))
    print(proxy_db.get_user_by_id(1))

    print(proxy_db.get_user_by_id(2))
