import Paragraph


class Chapter():

    def __init__(self, number, title, paragraphs):
        """A chapter consists of multiple paragraphs."""
        self.number = number
        self.title = title
        self.paragraphs = []
        for paragraph_lines in paragraphs:
            new_pragraph = Paragraph.Paragraph(paragraph_lines)
            self.paragraphs.append(new_pragraph)

    def read(self, paragraph_idx=None):
        """A paragraph can be read."""
        if paragraph_idx:
            self.paragraphs[paragraph_idx].read()
        else:
            for paragraph in self.paragraphs:
                paragraph.read()
