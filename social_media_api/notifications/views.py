from django.shortcuts import render
from .models import Notification

def get_notifications(request):
    notifications = request.user.notifications.filter(read=False).order_by("-created_at")
    return render(request, "notifications/list.html", {"notifications": notifications})
