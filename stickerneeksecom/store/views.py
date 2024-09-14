from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import render, get_object_or_404


def product(request, pk):
    # Get the product, or return a 404 error if not found
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product.html', {'product': product})

def category_list(request, slug=None):
    category = None
    subcategories = None

    if slug:
        # Get the category by slug (parent category)
        category = get_object_or_404(Category, slug=slug)
        # Get all subcategories of the parent category
        subcategories = category.children.all()
    else:
        # If no parent category is provided, list only root categories (parent is None)
        subcategories = Category.objects.filter(parent__isnull=True)
    
    return render(request, 'category_list.html', {
        'category': category,
        'subcategories': subcategories,
    })

# product = product.objects.all()
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def wholesale(request):
    return render(request, 'wholesale.html', {})