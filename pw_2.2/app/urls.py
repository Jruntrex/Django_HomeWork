from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>/<int:year>/', views.hello),
    path('hello2/', views.hello2),
    path('hello3/', views.hello3),
    path('comp/', views.comp),
    path('decomp/', views.decomp),
]
