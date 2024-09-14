from django.contrib import admin
from .models import Category, Customer, Product, Order

# Custom Admin Header
admin.site.site_header = 'Stickerneek Admin'
admin.site.site_title = 'Stickerneek Admin'
admin.site.index_title = 'Welcome to Stickerneek Admin'

# Define CategoryAdmin first
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'display_hierarchy')
    list_filter = ('parent',)  # Add filter by parent category

    def display_hierarchy(self, obj):
        """ 
        Display categories with an indentation that represents their depth in the hierarchy.
        """
        if obj.parent:
            return f"{'--' * self.get_category_depth(obj)} {obj.name}"
        return obj.name

    def get_category_depth(self, obj):
        """
        Calculate how deep a category is in the hierarchy based on its parents.
        """
        depth = 0
        while obj.parent:
            depth += 1
            obj = obj.parent
        return depth

    display_hierarchy.short_description = 'Category Hierarchy'  # Customize column name

# Now register models with their respective admins
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
