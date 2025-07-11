from facade_main import Author
from facade_main import Note
from facade_main import PreviewDelete
from facade_main import SaveNote


# Facade - allows user to simplify the use of a main codebase
# Just four plain methods contains all the functionality
class NoteInterface:
    def __init__(
        self, author: Author, note: Note, preview: PreviewDelete, save_note: SaveNote
    ):
        self.author = author
        self.note = note
        self.preview = preview
        self.save_note = save_note

    def show(self):
        self.preview.preview()

    def save(self, filename="notes.txt"):
        self.save_note.save(filename)

    def read(self, filename="notes.txt"):
        self.save_note.read(filename)

    def delete(self):
        self.preview.delete()


if __name__ == "__main__":
    author = Author.reg_author()
    note = Note(author, "My note", "Content of my note")
    preview = PreviewDelete(author, note.title, note.content)
    save_note = SaveNote(author, note.title, note.content)
    facade = NoteInterface(author, note, preview, save_note)
    facade.show()
    # facade.save()
    # facade.read()
