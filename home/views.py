from rest_framework.viewsets import ModelViewSet

from home.models import Category, Product, Seller, Cart
from home.serializers import CategoryModelSerializer, ProductModelSerializer, CartModelSerializer, SellerModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    """
    CRUD products
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class SellerModelViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerModelSerializer


# class CartModelViewSet(ModelViewSet):
