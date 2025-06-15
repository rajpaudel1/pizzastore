from django.db import models

# Create your models here.

from django.db import models 
  
  
class Order(models.Model): 
    cust_name = models.CharField(max_length=200) 
    address = models.TextField()
    items = models.CharField(max_length=200)
    is_delivered = models.CharField(max_length=200)
