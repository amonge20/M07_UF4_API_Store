from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.BooleanField(default=False)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    producte = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantitat = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')
