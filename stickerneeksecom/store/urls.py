from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wholesale', views.wholesale, name='wholesale'),
    path('product/<int:pk>', views.product, name='product'),
    path('collection/', views.collection, name='collection'),
    path('collection/<slug:slug>/', views.collection, name='collection'),
    ]
