from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = UserCreationForm()
        return render(request, "blog/register.html", {"form": form})

def home(request):
    return render(request, "blog/home.html")

def posts(request):
    return render(request, "blog/posts.html")
