from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from ..relationship_app.views import list_books, LibraryDetailView

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
