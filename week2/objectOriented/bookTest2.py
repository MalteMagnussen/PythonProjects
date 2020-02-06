import webget
import Book
import Chapter

bones_in_london_url = 'http://www.gutenberg.org/cache/epub/27525/pg27525.txt'
# download the book
webget.download(bones_in_london_url, 'bones_in_london.txt')
# open it and read all lines in the text file
with open('./bones_in_london.txt') as f:
    content = f.readlines()


def get_text(lower_bound, upper_bound):
    """A utility function which allow us to read slices of lines"""
    chapter_content = []
    paragraph = []
    for line in content[lower_bound:upper_bound]:
        if line == '\n':
            chapter_content.append(paragraph)
            paragraph = []
        else:
            paragraph.append(line.strip())

    return chapter_content


# Test
chapter_1 = Chapter.Chapter(1, 'Bones and Big Business', get_text(82, 762))
chapter_2 = Chapter.Chapter(2, 'Hidden Treassure', get_text(769, 1455))
book = Book.Book('Bones in London', 'Edgar Wallace', [chapter_1, chapter_2])

print(book.author)
print(book.title)
print(len(book.chapters))
