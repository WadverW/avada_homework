from datetime import datetime
import re


class Author:
    def __init__(self, name: str, surname: str, email: str):
        self.name = name
        self.surname = surname

        if self.email_valid(email):
            self.email = email
        else:
            return None

    @staticmethod
    def email_valid(email):
        pattern = r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return True

    @classmethod  # To refere to class via cls -> call email_valid in the class
    def reg_author(cls):
        while True:
            data = input("Enter your name, surname, email: ")
            vars = re.split(r"\s*[-,\s/;]+\s*", data)
            if len(vars) == 3:
                name, surname, email = vars

                try:
                    author = cls(name, surname, email)
                    return author
                except ValueError as e:
                    print(e)
                    continue
            else:
                print(
                    "Please enter name, surname, and email separated by spaces or comma"
                )
                continue


## Add Note - data stores in a dictionary
class Note:
    def __init__(self, author: Author, title: str, content: str, active: bool = True):
        self.note = {
            "author": author.name,
            "title": title,
            "content": content,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "active": active,
        }
        self.title = title
        self.content = content
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.active = active
        self._author = author

    def deactive(self):
        self.active = False
        return self.active

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.note["title"] = self._title

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.note["content"] = self._content


# With save() data is recorded in a file
# With read() data is read from a file
class SaveNote(Note):
    def __init__(self, author: Author, title: str, content: str, active: bool = True):
        super().__init__(author, title, content, active)

    def save(self, file_name: str):
        with open(file_name, "a", encoding="utf-8") as file:
            for key, value in self.note.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
        print("Note saved successfully!")

    def read(self, file_name: str):
        with open(file_name, "r", encoding="utf-8") as file:
            print(file.read())


# Opportunities: preview note, delete note from dictionary by title / deactivate note
class PreviewDelete(Note):
    def __init__(self, author: Author, title: str, content: str, active: bool = True):
        super().__init__(author, title, content, active)

    def preview(self):
        if self.active:
            print(
                f"__{self.title}__\n - {self.content}\n << {self._author.name} >> \n{self.date}"
            )
        else:
            print("Activate the note to preview it!")

    def delete(self):
        title = input("Enter the title to delete: ")
        if title == "":
            print("No title entered!")
            return
        if self.active:
            print(f"Are you sure you want to delete the note {title}?")
            to_delete = input("(y/n): ")
            if to_delete.strip().lower() == "y":
                try:
                    if title in self.note:
                        del self.note[title]
                        print("Note deleted successfully!")
                        return
                    else:
                        print("No such Title!")

                except KeyError:
                    print("Note not found!")

            else:
                print("Deletion canceled!")
        else:
            deactivate = input(f"Just deactivate the note {title}? (y/n): ")
            if deactivate.strip().lower() == "y":
                super().deactive()
                print("Note deactivated!")
                return


# if __name__ == "__main__":
#     author = Author("John", "Doe", "john.doe@example.com")

#     note = Note(author, "My First Note", "This is my first note.")
#     # note.save("notes.txt")
#     note.title = "Updated Title"
#     note.content = "My second note."

#     pd = PreviewDelete(author, note.title, note.content)
#     pd.preview()

#     save = SaveNote(author, note.title, note.content)
#     save.save("notes.txt")

# save.read("notes.txt")


# Цель: Предоставляет упрощённый интерфейс к сложной подсистеме.

# Принцип: Один класс скрывает множество внутренних.
