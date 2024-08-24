from bookshelf.models import Book
book.delete()
(1, {'bookshelf.Book': 1})

# Confirm that the book has been deleted
Book.objects.all()
<QuerySet []>

