from django.urls import path

from preg_form import views

urlpatterns = [
    path('', views.index),
    path('login/',views.reg_tb_entry),
    path('profile/',views.login)
]