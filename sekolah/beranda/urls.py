from django.urls import path
from beranda import views

urlpatterns = [
    path('', views.beranda, name='beranda')
]
