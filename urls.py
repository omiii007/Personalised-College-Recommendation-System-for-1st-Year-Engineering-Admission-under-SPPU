from django.contrib import admin
from django.urls import path
from projectApp import views


urlpatterns = [
   path("",views.index, name='projectApp'),
   path("index",views.index, name='index'),
   path("result", views.result, name='result'),
   path("input", views.input, name='input'),
   path("result_new", views.result, name='result_new'),
   path('signup', views.signup, name='signup'),
   path('login/', views.custom_login, name='login'),
   path('logout/', views.custom_logout, name='logout'),
   
]