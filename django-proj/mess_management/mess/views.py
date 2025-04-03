from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Meal
from .forms import MealForm

def meal_list(request):
    meals = Meal.objects.all()
    form = MealForm()

    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save()
            return JsonResponse({
                'id': meal.id,
                'name': meal.name,
                'price': str(meal.price),
                'date': str(meal.date)
            })

    return render(request, 'meal_list.html', {'meals': meals, 'form': form})

def update_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    
    if request.method == "POST":
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    meal.delete()
    return JsonResponse({'success': True, 'meal_id': meal_id})
