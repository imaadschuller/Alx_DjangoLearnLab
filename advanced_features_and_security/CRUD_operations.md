# CRUD Operations for the `Book` Model

This document summarizes the Create, Retrieve, Update, and Delete (CRUD) operations performed on the `Book` model using Django’s ORM.

## 1. Create Operation

### Command:
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
<Book: 1984>

## 2. Retrieve Operation

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
1984 George Orwell 1949

## 3. Update Operation

book.title = "Nineteen Eighty-Four"
book.save()
<Book: Nineteen Eighty-Four>

## 4. Delete Operation

book.delete()
(1, {'bookshelf.Book': 1})
Book.objects.all()
<QuerySet []>
