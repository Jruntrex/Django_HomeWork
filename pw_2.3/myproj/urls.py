from django.contrib import admin
from django.urls import path
from guessgame_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Головна сторінка гри. name='game_url' потрібен для функції redirect()
    path('guess/', views.game_page, name='game_url'),
    
    # Додатковий шлях для скидання гри
    path('reset/', views.reset_game),
]