from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import InventoryItem, ItemCategory
from .forms import InventoryItemForm, ItemCategoryForm

@login_required
def home(request):
    items = InventoryItem.objects.all().order_by('-date_added')  # Urutkan dari yang terbaru
    return render(request, 'main/home.html', {'items': items})

@login_required
def item_create(request):
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, request.FILES)  # Tambahkan request.FILES
        if form.is_valid():
            item = form.save(commit=False)
            item.added_by = request.user
            item.save()
            messages.success(request, 'Item berhasil ditambahkan!')
            return redirect('main:home')
    else:
        form = InventoryItemForm()
    
    context = {
        'form': form,
        'title': 'Tambah Item Baru'
    }
    return render(request, 'main/item_form.html', context)

@login_required
def item_update(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    
    if request.method == 'POST':
        form = InventoryItemForm(request.POST, request.FILES, instance=item)  # Tambahkan request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, 'Item berhasil diperbarui!')
            return redirect('main:home')
    else:
        form = InventoryItemForm(instance=item)
    
    context = {
        'form': form,
        'title': 'Edit Item',
        'item': item
    }
    return render(request, 'main/item_form.html', context)

@login_required
def item_delete(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Item berhasil dihapus!')
        return redirect('main:home')
    
    return render(request, 'main/item_confirm_delete.html', {'item': item})

@login_required
def item_detail(request, pk):
    item = get_object_or_404(InventoryItem, pk=pk)
    return render(request, 'main/item_detail.html', {'item': item})

@login_required
def category_list(request):
    categories = ItemCategory.objects.all().order_by('name')
    return render(request, 'main/category_list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil ditambahkan!')
            return redirect('main:category_list')
    else:
        form = ItemCategoryForm()
    
    context = {
        'form': form,
        'title': 'Tambah Kategori Baru'
    }
    return render(request, 'main/category_form.html', context)

@login_required
def category_update(request, pk):
    category = get_object_or_404(ItemCategory, pk=pk)
    
    if request.method == 'POST':
        form = ItemCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Kategori berhasil diperbarui!')
            return redirect('main:category_list')
    else:
        form = ItemCategoryForm(instance=category)
    
    context = {
        'form': form,
        'title': 'Edit Kategori'
    }
    return render(request, 'main/category_form.html', context)

@login_required
def category_delete(request, pk):
    category = get_object_or_404(ItemCategory, pk=pk)
    
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Kategori berhasil dihapus!')
        return redirect('main:category_list')
    
    return render(request, 'main/category_confirm_delete.html', {'category': category})