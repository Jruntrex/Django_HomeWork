from django.contrib import admin
from django.urls import path
from warehouse.views import product_list, replenish_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list),
    path('replenish/<int:count>/', replenish_products),
]