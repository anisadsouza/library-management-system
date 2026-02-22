from django.contrib import admin
from django.urls import path
from lms import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("home2/", views.home2, name="home2"),

    path("books/", views.books, name="books"),
    path("authors/", views.authors, name="authors"),

    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path("all_books/<str:books>/", views.all_books, name="all_books"),

    path("add-to-cart/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.my_cart, name="my_cart"),
    path("remove-from-cart/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
]