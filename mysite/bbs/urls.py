from django.urls import path
from . import views
from .views import SignUp
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', SignUp.as_view(template_name='signup.html'), name='signup'),
]
