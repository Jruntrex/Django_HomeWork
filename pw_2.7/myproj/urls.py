from django.contrib import admin
from django.urls import path
from instruments import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # READ
    path('products/', views.ProductListView.as_view(), name='product-list'),
    
    # CREATE
    path('products/add/', views.ProductCreateView.as_view(), name='product-create'),
    
    # UPDATE (pk - це Primary Key, тобто ID товару)
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-edit'),
    
    # DELETE
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    
    # REPLENISH (Генерація)
    path('replenish/<int:count>/', views.replenish, name='replenish'),
]