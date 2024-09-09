from django.shortcuts import render
from .models import Product

# product = product.objects.all()
def home(request):
    return render(request, 'home.html', {})