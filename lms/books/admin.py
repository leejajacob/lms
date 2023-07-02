from django.contrib import admin

from .models import Book, Cart, CartItems, Order

# Register your models here.
admin.site.register(Book)
admin.site.register(Order)