from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name = "register_url"),
    path('login/', views.login_view, name="login_url"),
    path('logout/', views.logout_view, name="logout_url")

]