from PythonProjects.utils import webget
from PythonProjects.week2.objectOriented.Book import Book
from PythonProjects.week2.objectOriented.Chapter import Chapter
from PythonProjects.week2.objectOriented import Paragraph
from PythonProjects.week2.objectOriented import ComicBook

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
chapter_1 = Chapter(1, 'Bones and Big Business', get_text(82, 762))
chapter_2 = Chapter(2, 'Hidden Treassure', get_text(769, 1455))
book = Book('Bones in London', 'Edgar Wallace', [chapter_1, chapter_2])

print(book.author)
print(book.title)
print(len(book.chapters))

# book.read(chapter=1)
book.open_book(chapter=2).read(paragraph_idx=3)
print("_______________________________________")
book.open_book(chapter=2).read(3)
print("_______________________________________")
print(book.__str__())

print("_______________________________________")
paragraph = Paragraph.Paragraph([])
print(paragraph.reading_position)

fst_paragraph = Paragraph.Paragraph([
    "Mrs. Staleyborn's first husband was a dreamy Fellow of a Learned",
    'University.']),
snd_paragraph = Paragraph.Paragraph([
    'Her second husband had begun life at the bottom of the ladder as a',
    'three-card trickster, and by strict attention to business and the',
    'exercise of his natural genius, had attained to the proprietorship of a',
    'bucket-shop.'])
snd_paragraph.read()
print(snd_paragraph.get_reading_position())

snd_paragraph.update_reading_position(3)

print(snd_paragraph.get_reading_position())

snd_paragraph.read()

print("SCROLLING: _______________________")

snd_paragraph.read()

snd_paragraph.scroll_down()
snd_paragraph.read()

snd_paragraph.scroll_down()
snd_paragraph.read()

snd_paragraph.scroll_down()
snd_paragraph.read()

snd_paragraph.scroll_down()
snd_paragraph.read()


print("SCROLLING: __________________________")
snd_paragraph.read()

snd_paragraph.scroll_up()
snd_paragraph.read()

snd_paragraph.scroll_up()
snd_paragraph.read()

snd_paragraph.scroll_up()
snd_paragraph.read()

print("\n\nCOMIC BOOK: \n")

comic = ComicBook.ComicBook('Le Grand Mort', 'Loisel')
print(comic.title)
