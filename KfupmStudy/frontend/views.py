from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from api.models import Student
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Create your views here.
@login_required(login_url= "login")
def home(request):
    return render(request, 'frontend/home.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))  

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "frontend/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "frontend/login.html") 

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "frontend/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = Student.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "frontend/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "frontend/register.html")
