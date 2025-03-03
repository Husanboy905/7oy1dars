# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('color/<int:color_id>/', views.car_by_color, name='car_by_color'),
#     path('brand/<int:brand_id>/', views.car_by_brand, name='car_by_brand'),
#     path('car/<int:car_id>/', views.car_detail, name='car_detail'),
#     path('car/<int:car_id>/comment/', views.add_comment, name='add_comment'),
#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
# ]
from django.urls import path
from .views import CarListView,CarByColorView,CarByBrandView,CarDetailView,AddCommentView,RegisterView,LoginView, LogoutView

urlpatterns = [
    path("", CarListView.as_view(), name="index"),
    path("color/<int:color_id>/", CarByColorView.as_view(), name="car_by_color"),
    path("brand/<int:brand_id>/", CarByBrandView.as_view(), name="car_by_brand"),
    path("car/<int:pk>/", CarDetailView.as_view(), name="car_detail"),
    path("car/<int:car_id>/comment/", AddCommentView.as_view(), name="add_comment"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
