from django.contrib.auth.models import User
from django.core.cache import cache
from django.db.models import Prefetch
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Category, Group, Product, Image, AttributeKey, AttributeValue, ProductAttribute
from .serializers import CategorySerializer, ProductSerializer, GroupSerializer, ProductImageSerializer, \
    AttributeKeySerializer, AttributeValueSerializer, ProductAttributeSerializer, UserSerializer


class CategoryListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer

    def get_queryset(self):
        cache_key = 'categories_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Category.objects.all()
            cache.set(cache_key, queryset, timeout=300)
        return queryset


class CategoryDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class GroupListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = GroupSerializer

    def get_queryset(self):
        cache_key = 'groups_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Group.objects.all()
            cache.set(cache_key, queryset, timeout=300)
        return queryset


class GroupDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    lookup_field = 'slug'


class ProductListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        cache_key = 'products_list'
        queryset = cache.get(cache_key)
        if queryset is None:
            queryset = Product.objects.select_related('group').all()
            queryset = queryset.select_related('group__category').all()
            cache.set(cache_key, queryset, timeout=300)
        return queryset


class ProductDetailView(RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = Product.objects.select_related('group').all()
        queryset = queryset.select_related('group__category').all()
        return queryset


class ImageListApiView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ProductImageSerializer


class AttributeKeyListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = AttributeKey.objects.all()
    serializer_class = AttributeKeySerializer


class AttributeValueListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = AttributeValue.objects.all()
    serializer_class = AttributeValueSerializer


class ProductAttributeListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer


class RegisterView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            return Response(status=204)
        except AttributeError:
            return Response({'error': 'User has no auth_token.'}, status=400)
