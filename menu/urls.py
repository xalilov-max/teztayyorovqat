from django.urls import path
from .views import FoodCategoryAPIView, FoodItemAPIView, OrderAPIView

urlpatterns = [
    path('categories/', FoodCategoryAPIView.as_view(), name='categories'),
    path('foods/', FoodItemAPIView.as_view(), name='foods'),
    path('orders/', OrderAPIView.as_view(), name='orders'),
]


# API Endpoints
# /api/categories/ - Manage food categories
# /api/foods/ - Manage food items
# /api/orders/ - Manage orders
