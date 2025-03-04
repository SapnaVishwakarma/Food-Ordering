from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from myapp.views import home
from myapp.views import ProductViewSet,RestaurantListCreateView, RestaurantRetrieveUpdateDestroyView, CategoryAPIView, CategoryDetailAPIView,RegisterAPIView, LoginAPIView


router = routers.DefaultRouter()
router.register(r'products',ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view(), name='restaurant-detail'),
    path('categories/', CategoryAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),   
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("", home, name="home"),  # This will serve React's index.html
]
