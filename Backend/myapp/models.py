from django.db import models
from django.contrib.auth.models import AbstractUser


# user models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

#creating Product model
class Product(models.Model):
    name=models.CharField(max_length=200)
    description = models.TextField()
    price =models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(
        max_length=100,
        choices=(('veg','veg'),('non-veg','non-veg'))
        )
    
    def __str__(self):
        return self.name  # Object ka readable name return karega

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name  

# Restaurant Model
#generic view used here
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    # opening_time = models.TimeField()  
    # closing_time = models.TimeField() 
    
    def __str__(self):
        return self.name  

#order model
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# Payment Model
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('upi', 'UPI'), ('cash', 'Cash')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"Payment {self.id} - {self.status}"

    
class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="cart_items", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    def __str__(self):
        return f"{self.product.name} ({self.quantity})"