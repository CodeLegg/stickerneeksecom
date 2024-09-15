from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product  # Ensure correct import



# product = product.objects.all()
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def wholesale(request):
    return render(request, 'wholesale.html', {})

def collection(request, slug=None):
    category = None
    products = None
    categories = Category.objects.exclude(name="CBD PACKAGING")  # Exclude the specific category

    if slug:
        try:
            # Look up the category by slug
            category = Category.objects.get(slug=slug)
            # Get all products directly related to this category
            products = Product.objects.filter(category=category)
        except Category.DoesNotExist:
            # Handle the case where the category does not exist
            messages.error(request, "That Category Doesn't Exist.")
            return redirect('collection')  # Redirect to the collection list if category doesn't exist

    context = {
        'category': category,
        'categories': categories,  # List all categories excluding "CBD PACKAGING"
        'products': products,  # Products for a specific category
    }

    return render(request, 'category.html', context)  # Replace with your actual template



def product(request,pk):
	product = Product.objects.get(id=pk)
	return render(request, 'product.html', {'product':product})