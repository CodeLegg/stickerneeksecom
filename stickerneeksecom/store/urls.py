from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale', views.wholesale, name='wholesale'),
    path('product/<int:pk>', views.product, name='product'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:slug>/', views.category_list, name='category_detail'),
]
