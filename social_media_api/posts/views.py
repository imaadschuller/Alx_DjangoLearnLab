from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType
class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return JsonResponse({'message': 'Post liked'})
    else:
        return JsonResponse({"message": "Post already liked"}, status=400)

def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return JsonResponse({'message': 'Post unliked'})
    except Like.DoesNotExist:
        return JsonResponse({"message": "Post not liked"})