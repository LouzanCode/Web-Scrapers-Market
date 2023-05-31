from django.urls import path, include
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carrito_total, name='carrito_total'),
    path('add/', views.carrito_add, name='carrito_add'),
    path('delete/', views.carrito_delete, name='carrito_delete'),
  
]