from django.db import models
import datetime

# Category / Collections

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, default='default-slug')
    description = models.TextField()
    image = models.ImageField(upload_to='category', null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Field to control the order

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['parent__id', 'order', 'id']  # Order by parent, then order field, then id

    def __str__(self):
        return self.name


# Customer / User

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Product / Item

class Product(models.Model):        
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=255, default='', blank=True)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='product', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

# Order / Transaction

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    address = models.CharField(max_length=255, default='', blank=True)
    phone = models.CharField(max_length=255, default='', blank=True)
    date_ordered = models.DateTimeField(datetime.datetime.today())
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=50, default='False')

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'{self.product.name} {self.customer.first_name}'