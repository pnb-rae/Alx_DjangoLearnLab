# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve the book by ID
book = Book.objects.get(id=1)

# Confirm retrieval
book
# <Book: 1984 by George Orwell (1949)>
```

