from django.urls import path
from .views import *
from . import views
# app_name = 'myapp'
urlpatterns = [
    path('login/',views.loginpage, name='login'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('register/', views.registerpage, name='registerpage'),
    path('home/', views.home, name='home'),

]