from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import InventoryItem, ItemCategory
from .forms import InventoryItemForm, ItemCategoryForm

@login_required
def home(request):
    items = InventoryItem.objects.all()
    return render(request, 'main/home.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()
            return redirect('home')
    else:
        form = InventoryItemForm()
    return render(request, 'main/item_form.html', {'form': form})

@login_required
def item_update(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = InventoryItemForm(instance=item)
    return render(request, 'main/item_form.html', {'form': form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'main/item_confirm_delete.html', {'item': item})

@login_required
def category_list(request):
    categories = ItemCategory.objects.all()
    return render(request, 'main/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ItemCategoryForm()
    return render(request, 'main/category_form.html', {'form': form})

@login_required
def category_update(request, pk):
    category = get_object_or_404(ItemCategory, pk=pk)
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = ItemCategoryForm(instance=category)
    return render(request, 'main/category_form.html', {'form': form})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(ItemCategory, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'main/category_confirm_delete.html', {'category': category})

@login_required
def item_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'main/item_detail.html', {'item': item})