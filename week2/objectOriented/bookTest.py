from PythonProjects.week2.objectOriented import Book

empty_book = Book.Book('The book of silence', 'Nobody')

print('Author:', empty_book.author)
print('Title:', empty_book.title)
print('Length of book:', len(empty_book.chapters), 'chapters')
