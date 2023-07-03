from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    image_url=models.CharField(max_length=2083,blank=True)
    book_available=models.BooleanField()
    quantity=models.PositiveIntegerField(default=0)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Book,max_length=200,null=True,on_delete=models.SET_NULL)
    order_date=models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    fine=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"Order #{self.id}"

    # def calculate_fine(self):
    #     if self.return_date and self.return_date > datetime.date.today():
    #         days_diff = (self.return_date - datetime.date.today()).days
    #         fine = days_diff * 2
    #         return fine
    #     return 0


class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    items=models.ManyToManyField(Book)


class CartItems(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)

