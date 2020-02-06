class Paragraph():
    """A paragraph consists of a list of lines."""

    def __init__(self, lines):
        """Initialize the paragraph with its lines of text."""
        self.lines = lines

    def read(self):
        """Simulate reading a paragraph by printing its contents."""
        for line in self.lines:
            print(line)
