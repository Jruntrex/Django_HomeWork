from django.contrib import admin
from django.urls import path
from maze import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('maze/', views.maze_view, name='maze'),
    path('maze/solve/', views.solve_view, name='solve'),
]