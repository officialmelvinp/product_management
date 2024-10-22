from django.contrib import admin
from django.urls import path, include
from product import routers as products_api_router
from product.viewsets import ProductViewSet

# Main API URL patterns
api_url_patterns = [
    path('products/', include(products_api_router.router.urls)),  # Product-related endpoints
    path('products/update/id/<int:pk>/', ProductViewSet.as_view({'put': 'update'}), name='update-product'),  # Update by ID
    path('products/update/name/', ProductViewSet.as_view({'put': 'update_product_by_name'}), name='update-product-by-name'),  # Update by name
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'}), name='retrieve-product-id'),  # Retrieve by ID
    path('products/name/', ProductViewSet.as_view({'get': 'retrieve_product_by_name'}), name='retrieve-product-name'),  # Retrieve by name
    path('products/delete/name/', ProductViewSet.as_view({'delete': 'delete_by_name'}), name='delete-by-name'),  # Delete by name
    path('products/delete/id/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'}), name='delete-by-id'),  # Delete by ID
]

# URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel route
    path('api/', include(api_url_patterns)),  # Base API path for the API
]
