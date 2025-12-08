from django.contrib import admin
from django.urls import path
from math_service.views import calculate_factorial

urlpatterns = [
    path('admin/', admin.site.urls),
    path('factorial/<int:n>/', calculate_factorial),
]