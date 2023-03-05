from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from home.models import Seller, Cart, Product, Category


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ()


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class SellerModelSerializer(ModelSerializer):
    class Meta:
        model = Seller
        exclude = ()


class CartModelSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Cart
        exclude = ()
