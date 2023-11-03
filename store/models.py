from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    def __str__(self):
        return f"{self.name}-{self.price}-{self.quantity}"

class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return f"{self.user}-{self.paid}-{self.product}-{self.quantity}"
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    order_details = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user}-{self.order_details.paid}-{self.created }"


