from django.urls import path
from . import views

app_name = 'main'  # Penting karena kamu pakai 'main:home' di views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/create/', views.item_create, name='item_create'),
    path('items/<int:pk>/update/', views.item_update, name='item_update'),
    path('items/<int:pk>/delete/', views.item_delete, name='item_delete'),
    path('items/<int:pk>/', views.item_detail, name='item_detail'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
]