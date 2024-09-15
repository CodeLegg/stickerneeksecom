from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product  # Ensure correct import

def collection(request, slug=None):
    category = None
    products = None

    if slug:
        try:
            # Look up the category by slug
            category = Category.objects.get(slug=slug)
            # Get all products directly related to this category
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            # Handle the case where the category does not exist
            messages.error(request, "That category doesn't exist...")
            return redirect('home')

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category.html', context)  # Replace with your actual template

def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})

# product = product.objects.all()
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def wholesale(request):
    return render(request, 'wholesale.html', {})