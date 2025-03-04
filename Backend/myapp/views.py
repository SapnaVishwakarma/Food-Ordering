from django.shortcuts import render
from rest_framework import viewsets, generics
from myapp.models import Product,Restaurant,Category
from myapp.serializers import ProductSerializer, RestaurantSerializer,CategorySerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny,IsAuthenticated

from django.shortcuts import render

def home(request):
    return render(request , 'index.html')


# Create your views here.
#Model view of product
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

#API View 
# class LoginAPi(APIView):
#     def post(self, reqest):

#Generic view of restaurant
#for list and create restaurant api
class RestaurantListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class =RestaurantSerializer

    def get(self, request, *args, **kwargs):
        print("Authorization Header:", request.headers.get('Authorization'))  # Debugging
        return super().get(request, *args, **kwargs)

class RestaurantRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

#Category
#API View 
class CategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]  
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]  

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return None
    def get(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return JsonResponse({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return JsonResponse({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            category = serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)  # Return updated record
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if not category:
            return JsonResponse({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return JsonResponse({"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT)

#Register
class RegisterAPIView(APIView):
    permission_classes = []  # No authentication required for registration
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LOGIN API
class LoginAPIView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to access
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)  # Check credentials
        if user:
            token, _ = Token.objects.get_or_create(user=user)  # Generate token
            return Response({"message": "Login successful!", "token": token.key}, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)