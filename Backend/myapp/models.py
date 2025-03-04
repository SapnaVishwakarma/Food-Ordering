from django.db import models


# Create your models here.

#creating Product model
class Product(models.Model):
    product_id =models.AutoField(primary_key=True)
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

# Payment Model
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('upi', 'UPI'), ('cash', 'Cash')])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.name  
    
class CartItem(models.Model):
    product = models.ForeignKey('myapp.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
   
    def __str__(self):
        return self.name  