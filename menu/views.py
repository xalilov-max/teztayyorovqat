from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodCategory, FoodItem, Order
from .serializers import FoodCategorySerializer, FoodItemSerializer, OrderSerializer
from .permissions import IsAdminOrReadOnly

class FoodCategoryAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        categories = FoodCategory.objects.all()
        serializer = FoodCategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FoodCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodItemAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        foods = FoodItem.objects.all()
        serializer = FoodItemSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = FoodItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderAPIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
