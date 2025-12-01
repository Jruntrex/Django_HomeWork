from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Головне завдання 2.4
    path('hello/<str:name>/<int:year>/', views.hello),

    # Старі маршрути
    path('hello2/', views.hello2),
    path('hello3/', views.hello3),
    path('comp/', views.comp),
    path('decomp/', views.decomp),
]