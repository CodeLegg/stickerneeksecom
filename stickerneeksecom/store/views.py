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
    subcategory_products = []

    if slug:
        # Get the selected category by slug
        category = get_object_or_404(Category, slug=slug)
        # Get all products directly related to this category
        products = Product.objects.filter(category=category)
        
        # Recursively get all descendants of this category
        def get_subcategory_products(category):
            subcategory_products = []
            subcategories = category.children.all()

            for subcategory in subcategories:
                # Get products for each subcategory
                products_for_subcategory = Product.objects.filter(category=subcategory)
                # Recursively fetch the descendants of this subcategory
                descendants = get_subcategory_products(subcategory)

                subcategory_products.append({
                    'subcategory': subcategory,
                    'products': products_for_subcategory,
                    'descendants': descendants
                })
            return subcategory_products

        # Get all subcategory products recursively for the main category
        subcategory_products = get_subcategory_products(category)

    else:
        # If no slug, show top-level categories (with no parent)
        subcategories = Category.objects.filter(parent__isnull=True)

    context = {
        'category': category,
        'products': products,
        'subcategory_products': subcategory_products,
    }

    return render(request, 'category.html', context)


# product = product.objects.all()
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def wholesale(request):
    return render(request, 'wholesale.html', {})