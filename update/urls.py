from django.contrib import admin
from django.urls import path, include
from product import routers as products_api_router
from product.viewsets import ProductViewSet

# Main API URL patterns
api_url_patterns = [
    path('products/', include(products_api_router.router.urls)),  # Product-related endpoints
    path('products/update/', ProductViewSet.as_view({'put': 'update'}), name='update-product'),
    path('products/delete/', ProductViewSet.as_view({'delete': 'delete_by_name'}), name='delete-by-name'),
]

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_url_patterns)),  # Base API path
]
