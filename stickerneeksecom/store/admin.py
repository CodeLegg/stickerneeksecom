from django.contrib import admin
from .models import Category, Customer, Product, Order

admin.site.site_header = 'Stickerneek Admin'
admin.site.site_title = 'Stickerneek Admin'
admin.site.index_title = 'Welcome to Stickerneek Admin'

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
