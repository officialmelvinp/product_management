from django.contrib import admin
from .models import Product

# Register the Product model in the Django admin site
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ['id', 'name']
    # Add a search box to filter products by name
    search_fields = ['name']
    # Add filters to the right side for easier navigation (if needed in the future)
    list_filter = ['name']
