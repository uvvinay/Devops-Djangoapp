from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=20, null=True, blank=True)
    email=models.EmailField(max_length=30, null=True, blank=True)
    mobile=models.BigIntegerField(null=True, blank=True)
    location=models.CharField(max_length=30, null=True, blank=True)
    profile_pic=models.ImageField(blank=True,null=True)

class Products(models.Model):
    CATEGORY_CHOICE=(
        ('Indoor','Indoor'),
        ('Anywhere','Anywhere'),
        ('Outdoor','Outdoor'),
    )
    name=models.CharField(max_length=30)
    price =models.IntegerField()
    description=models.CharField(max_length=100, null=True)
    category=models.CharField(choices=CATEGORY_CHOICE, max_length=50)
    Order_date=models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    STATUS_CHOICES = (
        ('Delivered','Delivered'),
        ('Pending','Pending'),
        ('OutforDelivered','OutforDelivered')
    )
    customer= models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(Products, null=True, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS_CHOICES, max_length=30)
    order_date=models.DateField(auto_now=True)

