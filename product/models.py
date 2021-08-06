from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator


User=get_user_model()

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    name = models.CharField(max_length=200,unique=True)
    thumbnail = models.ImageField(upload_to='products/thumbnail')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    created_at =models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
