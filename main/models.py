from django.db import models
from accounts.models import CustomUser

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
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.quantity})"