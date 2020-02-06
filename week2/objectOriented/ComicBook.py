import Book


class ComicBook(Book.Book):
    def __init__(self, title, author, chapters=[]):
        """Initialize attributes of the parent class."""
        super().__init__(title, author, chapters=chapters)
