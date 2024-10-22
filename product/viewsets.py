from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # Create a new product
    def create(self, request):
        serializer = ProductSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Product created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve all products or retrieve a product by name
    def list(self, request):
        name = request.query_params.get('name', None)
        if name:
            product = get_object_or_404(Product, name=name)
            serializer = ProductSerializer(product, context={'request': request})
            return Response({
                "message": "Product retrieved successfully",
                "data": serializer.data
            })
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True, context={'request': request})
            return Response(serializer.data)

    # Retrieve a product by ID
    def retrieve(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response({
            "message": "Product retrieved successfully",
            "data": serializer.data
        })

    # Retrieve a product by name
    def retrieve_product_by_name(self, request):
        name = request.query_params.get('name', None)
        product = get_object_or_404(Product, name=name)
        serializer = ProductSerializer(product, context={'request': request})
        return Response({
            "message": "Product retrieved successfully",
            "data": serializer.data
        })

    # Update a product (PUT request)
    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Product updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update a product by name
    def update_product_by_name(self, request):
        name = request.query_params.get('name')
        product = get_object_or_404(Product, name=name)
        
        serializer = ProductSerializer(product, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Product updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a product by name
    def delete_by_name(self, request):
        name = request.query_params.get('name', None)
        product = get_object_or_404(Product, name=name)
        product.delete()
        return Response({
            "message": "Product deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

    # Delete a product by ID
    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({
            "message": "Product deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)
