from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
     path('admin/', admin_view(template_name=admin_view.html), name='admin_view'),
    path('librarian/', librarian_view(template_name=librarian_view.html), name='librarian_view'),
    path('member/', member_view(template_name=member_view.html), name='member_view'),
    path('book/add/', add_book, name='add_book'),
    path('book/edit/<int:pk>/', edit_book, name='edit_book'),
    path('book/delete/<int:pk>/', delete_book, name='delete_book'),
]
