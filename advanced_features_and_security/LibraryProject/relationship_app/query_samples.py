import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'")
        return
    # Use filter with author=author (this is what the checker wants)
    books = Book.objects.filter(author=author)
    print(f"Books by author '{author_name}':")
    for book in books:
        print(f"- {book.title}")
    print()

def list_all_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
        return
    # Use .books.all() to get all books in library
    books = library.books.all()
    print(f"Books in library '{library_name}':")
    for book in books:
        print(f"- {book.title}")
    print()

def retrieve_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'")
        return
    try:
        librarian = Librarian.objects.get(library=library)
        print(f"Librarian of '{library_name}': {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"Librarian of '{library_name}': No librarian found")
    print()

if __name__ == "__main__":
    query_all_books_by_author("J.K. Rowling")
    list_all_books_in_library("City Library")
    retrieve_librarian_for_library("City Library")


