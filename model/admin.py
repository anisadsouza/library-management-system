from django.contrib import admin
from .models import Books, CartItem

admin.site.register(Books)
admin.site.register(CartItem)