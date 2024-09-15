from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostCreateView, PostDeleteView, PostDetailView, PostUpdateView
urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="blog/registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/registration/logout.html"), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("", views.home, name="home"),
    path("posts/", views.posts, name="posts"),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk/comments/new/', views.add_comment_to_post, name='add-comment'),
    path('comment/<int:pk>/update/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]
