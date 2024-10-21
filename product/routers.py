from rest_framework import routers
from .viewsets import ProductViewSet

app_name = "products"

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')  # Registering the ProductViewSet
