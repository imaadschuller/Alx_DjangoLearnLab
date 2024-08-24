Django Permissions and Groups Setup

This guide explains how to configure and use permissions and groups in the Django application to manage user access.

1. Custom Permissions

Permissions control actions on models. For the "Book" model, permissions are defined as follows:

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField(default=2024)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
2. Groups and Permissions
Create Groups in the Django Admin Panel:

"Editors", "Viewers", "Admins".
Assign Permissions to Groups:

Editors: can_edit, can_create.
Viewers: can_view.
Admins: All permissions.

3. Enforcing Permissions in Views
Use @permission_required decorator to enforce permissions:

python
Copy code
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    return render(request, 'relationship_app/create_book.html')

4. Testing Permissions
Create Test Users and assign them to different groups.
Verify Access by logging in as these users and checking if permissions are correctly enforced.

