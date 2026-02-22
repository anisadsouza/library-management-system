from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from model.models import CartItem, Books


# ---------------------------
# Pages
# ---------------------------

def home(request):
    return render(request, "home.html")


@login_required
def home2(request):
    return render(request, "home2.html")


def authors(request):
    return render(request, "authors.html")


def books(request):
    # Keep categories exactly as your URLs use them
    categories = ["Philosophy", "Mythology", "Science and Fiction", "Non Fiction", "Marathi"]
    return render(request, "books.html", {"categories": categories})


# ---------------------------
# Authentication
# ---------------------------

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:
            messages.error(request, "Please enter both username and password.")
            return render(request, "login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("home2")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()
        confirm_password = request.POST.get("confirm_password", "").strip()

        if not username or not password or not confirm_password:
            messages.error(request, "Please fill all fields.")
            return render(request, "register.html")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Registration successful. Please log in.")
        return redirect("login")

    return render(request, "register.html")


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect("home")


# ---------------------------
# Books by category
# ---------------------------

def all_books(request, books):
    filtered_books = Books.objects.filter(book_type=books)
    return render(request, "all_books.html", {"books": filtered_books, "category": books})


# ---------------------------
# Cart
# ---------------------------

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    CartItem.objects.get_or_create(user=request.user, book=book)
    return redirect(reverse("all_books", args=[book.book_type]))


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect("my_cart")


@login_required
def my_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.book.price for item in cart_items)
    return render(request, "my_books.html", {"cart_items": cart_items, "total": total})