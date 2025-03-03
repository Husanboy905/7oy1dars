# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from .models import Cars, Comment, Colors, Brands
# def index(request):
#     cars = Cars.objects.all()
#     return render(request, 'index.html', {'cars': cars})
#
# def car_by_color(request, color_id):
#     color = get_object_or_404(Colors, id=color_id)
#     cars = Cars.objects.filter(color=color)
#     return render(request, 'index.html', {'cars': cars, 'filter': f"Color: {color.name}"})
#
# def car_by_brand(request, brand_id):
#     brand = get_object_or_404(Brands, id=brand_id)
#     cars = Cars.objects.filter(brand=brand)
#     return render(request, 'index.html', {'cars': cars, 'filter': f"Brand: {brand.name}"})
#
# def car_detail(request, car_id):
#     car = get_object_or_404(Cars, id=car_id)
#     return render(request, 'car_detail.html', {'car': car})
#
# @login_required
# def add_comment(request, car_id):
#     car = get_object_or_404(Cars, id=car_id)
#     if request.method == "POST":
#         text = request.POST.get("text")
#         if text:
#             Comment.objects.create(car=car, user=request.user, text=text)
#     return redirect('car_detail', car_id=car.id)
#
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})
#
# def user_login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('index')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})
#
# def user_logout(request):
#     logout(request)
#     return redirect('index')



from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404
from .models import Cars, Colors,Brands,Comment
from django.views import View
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



class CarListView(ListView):
    model = Cars
    template_name = "index.html"
    context_object_name = "cars"




class CarByColorView(ListView):
    model = Cars
    template_name = "index.html"
    context_object_name = "cars"

    def get_queryset(self):
        color = get_object_or_404(Colors, id=self.kwargs["color_id"])
        return Cars.objects.filter(color=color)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        color = get_object_or_404(Colors, id=self.kwargs["color_id"])
        context["filter"] = f"Color: {color.name}"
        return context




class CarByBrandView(ListView):
    model = Cars
    template_name = "index.html"
    context_object_name = "cars"

    def get_queryset(self):
        brand = get_object_or_404(Brands, id=self.kwargs["brand_id"])
        return Cars.objects.filter(brand=brand)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand = get_object_or_404(Brands, id=self.kwargs["brand_id"])
        context["filter"] = f"Brand: {brand.name}"
        return context



class CarDetailView(DetailView):
    model = Cars
    template_name = "car_detail.html"
    context_object_name = "car"





@method_decorator(login_required, name="dispatch")
class AddCommentView(View):
    def post(self, request, car_id):
        car = get_object_or_404(Cars, id=car_id)
        text = request.POST.get("text")
        if text:
            Comment.objects.create(car=car, user=request.user, text=text)
        return redirect("car_detail", car_id=car.id)






class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response




class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
        return render(request, "login.html", {"form": form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")
