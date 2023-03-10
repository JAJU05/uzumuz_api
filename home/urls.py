from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet, SellerModelViewSet

router = DefaultRouter()
router.register('products', ProductModelViewSet, 'products')
router.register('category', CategoryModelViewSet, 'category')
router.register('seller', SellerModelViewSet, 'seller')

urlpatterns = [
    path('', include(router.urls)),
]
