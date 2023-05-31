from django.urls import path, include
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    path('categories/<slug:category_slug>/', views.category_list, name='category_list'),
  
]