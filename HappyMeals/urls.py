#App urls
from django.contrib import admin
from django.urls import path
from HappyMeals import views
urlpatterns = [
    path('',views.index,name="index"),
    path('sign_in', views.sign_in,name="sign in"),
    path('sign_up',views.sign_up,name="Sign up"),
    path('order', views.order,name="order")
]