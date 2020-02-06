class Paragraph():
    """A paragraph consists of a list of lines."""

    def __init__(self, lines):
        """Initialize the paragraph with its lines of text."""
        self.lines = lines
        self.reading_position = 0

    def read(self):
        """Simulate reading a paragraph by printing its contents."""
        # for line in self.lines:
        #     print(line)
        print(self.lines[self.reading_position])

    def get_reading_position(self):
        return self.reading_position

    def update_reading_position(self, new_position):
        if new_position <= len(self.lines) - 1:
            self.reading_position = new_position

    def scroll_down(self):
        if self.reading_position < len(self.lines) - 1:
            self.reading_position += 1
        else:
            self.reading_position = 0

    def scroll_up(self):
        if self.reading_position >= 1:
            self.reading_position -= 1
        else:
            self.reading_position = len(self.lines) - 1
