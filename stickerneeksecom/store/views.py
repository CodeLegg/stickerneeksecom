from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404


def product(request, pk):
    # Get the product, or return a 404 error if not found
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def category(request, slug=None):
    category = None
    products = None
    subcategories = None

    if slug:
        # Get the selected category by slug
        category = get_object_or_404(Category, slug=slug)
        # Get all products related to this category and its subcategories
        products = Product.objects.filter(category=category)  # Products in this category

        # Get subcategories of this category (children)
        subcategories = category.children.all()
        
        # Optionally, fetch products for all subcategories too
        all_subcategory_products = Product.objects.filter(category__in=subcategories)

    else:
        # If no slug, show top-level categories (with no parent)
        subcategories = Category.objects.filter(parent__isnull=True)

    return render(request, 'category.html', {
        'category': category,
        'products': products,
        'subcategories': subcategories,
        'all_subcategory_products': all_subcategory_products,  # For additional subcategory products
    })

# product = product.objects.all()
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def wholesale(request):
    return render(request, 'wholesale.html', {})