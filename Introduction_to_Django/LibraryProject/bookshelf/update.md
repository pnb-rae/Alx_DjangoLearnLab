# Update Book Title

```python
from bookshelf.models import Book

# Retrieve the book by ID
book = Book.objects.get(id=1)

# Update the title
book.title = "Nineteen Eighty-Four"

# Save the updated book
book.save()

# Confirm the update
Book.objects.all()
# <QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
```


