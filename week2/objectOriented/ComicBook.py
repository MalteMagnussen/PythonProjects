import Book

# Inheritance example


class ComicBook(Book.Book):
    def __init__(self, title, author, chapters=[]):
        """Initialize attributes of the parent class."""
        super().__init__(title, author, chapters=chapters)
        self.images = []

    def get_images(self):
        return self.images

# overwrite example
    def __repr__(self):
        return 'ComicBook(%r, %r, %r)' % (self.title, self.author,
                                          self.chapters)
