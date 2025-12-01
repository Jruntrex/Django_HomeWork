from django.contrib import admin
from django.urls import path
from guessgame_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('guess/', views.game_page, name='game_url'),
    
    path('reset/', views.reset_game),
]