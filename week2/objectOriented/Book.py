import Chapter


class Book():
    """A simple book model consisting of chapters, which in 
    turn consist of paragraphs."""

    def __init__(self, title, author, chapters=[]):
        """Initialize title, the author, and the chapters."""
        self.title = title
        self.author = author
        self.chapters = chapters

    def __repr__(self):
        return 'Book(%r, %r, %r)' % (self.title, self.author, self.chapters)

    def __str__(self):
        return '{name} by {by} has {nr_chap} chapters.'.format(
            name=self.title, by=self.author, nr_chap=len(self.chapters))

    def read(self, chapter=1):
        """Simulate reading a chapter, by calling the reading 
        method of a chapter."""
        self.chapters[chapter - 1].read()

    def open_book(self, chapter=1) -> Chapter:
        """Simulate opening a book, which returns a chapter 
        object."""
        return self.chapters[chapter - 1]
