from django.contrib import admin
from django.urls import path
from tasks.views import factorial_input, factorial_result, feedback_form, rating_page

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Блок факторіала
    path('factorial/', factorial_input),
    path('result/', factorial_result),
    
    # Блок відгуків
    path('feedback/', feedback_form),
    path('rating/', rating_page),
]