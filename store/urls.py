from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from . import views, auth_view

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('products', views.ProductViewSet, basename='product')
router.register('orders', views.OrderViewSet, basename='order')
router.register('orderitems', views.OrderItemViewSet, basename='orderitem')
router.register('cart', views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', auth_view.register),
]
