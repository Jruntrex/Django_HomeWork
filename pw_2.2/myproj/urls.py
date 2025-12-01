from django.contrib import admin
from django.urls import path
from app import views  # Імпортуємо твої views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Завдання 1: <int:year> важливо!
    path('hello/<str:name>/<int:year>/', views.hello),

    # Завдання 2
    path('hello2/', views.hello2),

    # Завдання 3
    path('hello3/', views.hello3),

    # Завдання 4
    path('comp/', views.comp),
    path('decomp/', views.decomp),
]