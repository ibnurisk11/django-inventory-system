from django.db import models
from django.conf import settings

class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='inventory_images/', null=True, blank=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.quantity})"