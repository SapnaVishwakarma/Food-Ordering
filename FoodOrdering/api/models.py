from django.db import models

# Create your models here.

#creating Product model
class Product(models.Model):
    product_id =models.AutoField(primary_key=True)
    name=models.ChartField(max_length=200)
    description = models.TimeField()
    price =models.DecimalField(max_digits=10, decimal_places=2)
    type=models.CharField(max_length=100,choices=(('Veg','Veg'),('non-veg','non-veg')))


