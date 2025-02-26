from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Cars, Comment, Colors, Brands
def index(request):
    cars = Cars.objects.all()
    return render(request, 'index.html', {'cars': cars})

def car_by_color(request, color_id):
    color = get_object_or_404(Colors, id=color_id)
    cars = Cars.objects.filter(color=color)
    return render(request, 'index.html', {'cars': cars, 'filter': f"Color: {color.name}"})

def car_by_brand(request, brand_id):
    brand = get_object_or_404(Brands, id=brand_id)
    cars = Cars.objects.filter(brand=brand)
    return render(request, 'index.html', {'cars': cars, 'filter': f"Brand: {brand.name}"})

def car_detail(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    return render(request, 'car_detail.html', {'car': car})

@login_required
def add_comment(request, car_id):
    car = get_object_or_404(Cars, id=car_id)
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            Comment.objects.create(car=car, user=request.user, text=text)
    return redirect('car_detail', car_id=car.id)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('index')
