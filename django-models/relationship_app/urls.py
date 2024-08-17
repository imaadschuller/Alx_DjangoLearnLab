from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]
