from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Product
import random

# === GENERIC VIEWS (CRUD) ===

# 1. READ: Список товарів
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html' # вказуємо назву шаблону
    context_object_name = 'products'    # як звертатись до списку в HTML

# 2. CREATE: Створення товару
class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_form.html'
    fields = ['name', 'instrument_type', 'brand', 'material', 'price']
    success_url = reverse_lazy('product-list') # куди перенаправити після успіху

# 3. UPDATE: Редагування товару
class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_form.html' # використовуємо ту ж форму, що і для створення
    fields = ['name', 'instrument_type', 'brand', 'material', 'price']
    success_url = reverse_lazy('product-list')

# 4. DELETE: Видалення товару
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

# === ФУНКЦІОНАЛЬНИЙ VIEW (для авто-генерації) ===
def replenish(request, count):
    brands = ['Fender', 'Gibson', 'Yamaha', 'Ibanez', 'Roland', 'Moog']
    types = ['Гітара', 'Синтезатор', 'Барабани', 'Скрипка', 'Бас-гітара']
    materials = ['Дерево (Клен)', 'Дерево (Махагоні)', 'Пластик', 'Метал']
    
    products_to_create = []
    for i in range(count):
        products_to_create.append(Product(
            name=f"Model-{random.randint(100, 999)}",
            instrument_type=random.choice(types),
            brand=random.choice(brands),
            material=random.choice(materials),
            price=random.uniform(100.00, 5000.00)
        ))
    
    Product.objects.bulk_create(products_to_create)
    
    return HttpResponse(f"Успішно додано {count} інструментів! <a href='/products/'>Назад до списку</a>")