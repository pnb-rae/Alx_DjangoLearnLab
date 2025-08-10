import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        return books
    except Author.DoesNotExist:
        return []

# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None

if __name__ == '__main__':
    # Example data (replace with real data from your database)
    author_name = 'J.K. Rowling'
    library_name = 'City Library'

    books_by_author = get_books_by_author(author_name)
    print(f"Books by author '{author_name}':")
    for book in books_by_author:
        print(f"- {book.title}")

    books_in_library = get_books_in_library(library_name)
    print(f"\nBooks in library '{library_name}':")
    for book in books_in_library:
        print(f"- {book.title}")

    librarian = get_librarian_for_library(library_name)
    print(f"\nLibrarian of '{library_name}': {librarian.name if librarian else 'No librarian found'}")

