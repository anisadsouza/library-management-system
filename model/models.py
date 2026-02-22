from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    title = models.CharField(max_length=255)
    book_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=100, default="default.png")

    def __str__(self):
        return self.title


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.CharField(max_length=255, blank=True)  # keep because migration exists

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"