from django import forms
from .models import InventoryItem, ItemCategory

class InventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ['name', 'category', 'quantity', 'location', 'description', 'image']  # <-- Tambahkan 'image'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ItemCategoryForm(forms.ModelForm):
    class Meta:
        model = ItemCategory
        fields = ['name', 'description']