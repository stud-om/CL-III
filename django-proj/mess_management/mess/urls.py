from django.urls import path
from .views import meal_list, update_meal, delete_meal

urlpatterns = [
    path('', meal_list, name='meal_list'),
    path('update/<int:meal_id>/', update_meal, name='update_meal'),
    path('delete/<int:meal_id>/', delete_meal, name='delete_meal'),
]
