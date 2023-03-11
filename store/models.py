from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    C_ID = models.IntegerField(primary_key=True, max_length=25)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(default='default.jpg', upload_to='customer_image', null=True)
    Address = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    User = models.ForeignKey(User, on_delete=models.CASCADE)


class Product(models.Model):
    Pr_ID = models.IntegerField(primary_key=True)
    Pr_Name = models.CharField(max_length=100)
    Brand = models.CharField(max_length=50)
    Price = models.FloatField(max_length=8)
    Category = models.CharField(max_length=50)
    Image = models.ImageField(default='default.jpg', upload_to='product_image', null=True)
    Description = models.CharField(max_length=500)


class Order(models.Model):
    O_ID = models.IntegerField(primary_key=True)
    Cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Cust_Name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    Address = models.CharField(max_length=200)
    Payment_Status = models.CharField(max_length=6)


class Payment(models.Model):
    Payment_ID = models.IntegerField(primary_key=True)
    Ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    Method = models.CharField(max_length=10)
    Amount = models.FloatField(max_length=8)


class Cart(models.Model):
    Cart_ID = models.IntegerField(primary_key=True)
    Cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Prod = models.ForeignKey(Product, on_delete=models.CASCADE)


class Reviews(models.Model):
    Review_ID = models.IntegerField(primary_key=True)
    Prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    Cust = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Rating = models.FloatField(max_length=3)
    Review_Details = models.CharField(max_length=500)
    Image = models.ImageField(default='default.jpg', upload_to='review_image', null=True)
