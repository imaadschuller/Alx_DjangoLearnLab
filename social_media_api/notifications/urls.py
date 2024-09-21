from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notifications, name='notifications_list'),
    path('notifications/', views.get_notifications, name='notifications'),

]
